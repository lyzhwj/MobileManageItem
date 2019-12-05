from flask import render_template, request, redirect, url_for, session

from apps.decorate import login_required
from apps.model import Project, History, User, db, Dictionary, Officer
from apps.workListView import wkl

per_page = 1  # 每页数量

@wkl.route('/to_be_audited/', methods=['POST', 'GET'])  # 待审核工作
@login_required
def to_be_audited():
    if request.method == 'GET':
        uid = session.get('user')  # 通过session获取uid
        page = int(request.args.get('page', 1))  # url传参
        offices = Officer.query.filter(Officer.uid == uid).all()
        pids = []
        for office in offices:
            pids.append(office.pid)
        paginate = Project.query.filter(Project.id.in_(pids),
                                        Project.status == 22).paginate(page=page, per_page=per_page, error_out=False)
        return render_template('workList/to_be_audited.html', paginate=paginate)


@wkl.route('/operate/', methods=['POST', 'GET'])  # 审核工作
@login_required
def operation():
    uid = session.get('id')
    if User.query.get(uid).rid > 1:
        pid = int(request.args.get('pid', default=0))
        if pid == 0:
            return redirect(url_for('workListView.to_be_audited'))
        project = Project.query.get(pid)
        if request.method == 'GET':
            histories = History.query.filter(History.pid == pid)
            flag = histories.count()
            return render_template('workList/operate.html', project=project, histories=histories, flag=flag)

        # POST 提交操作
        status = int(request.form.get("status"))  # 链接中把status的状态放入url
        info = request.form.get("info")
        project.status = status

        th = History(pid=pid, info=info, uid=uid, status=status)
        db.session.add(th)
        db.session.commit()
        return redirect(url_for('workListView.to_be_audited'))
    return redirect(url_for('workListView.to_be_audited'))


@wkl.route('/to_be_revised/', methods=['GET'])  # 待修改工作
@login_required
def to_be_revised():
    uid = session.get('user')
    page = int(request.args.get('page', 1))
    paginate = Project.query.filter(Project.uid == uid,
                                    Project.status == 24).paginate(page=page, per_page=per_page, error_out=False)
    return render_template('workList/to_be_revised.html', paginate=paginate)


@wkl.route('/revise/', methods=['POST', 'GET'])  # 修改工作
@login_required
def revise():
    pid = request.args.get('pid', 0)
    if pid == 0:
        return redirect(url_for('workListView.to_be_revised'))  # 重定向
    project = Project.query.get(pid)

    if request.method == 'GET':
        histories = History.query.filter(History.pid == pid)
        flag = histories.count()
        return render_template('workList/revise.html', project=project, histories=histories, flag=flag)

    project.status = request.form.get('status')  # 通过url传参
    project.info = request.form.get('info')
    db.session.commit()
    return redirect(url_for('workListView.to_be_revised'))


@wkl.route('/to_be_seen/', methods=['GET'])  # 待查看工作
@login_required
def to_be_seen():
    page = int(request.form.get('page', 1))
    uid = session.get('user')
    if request.method == 'GET':
        paginate = Project.query.filter(Project.uid == uid,
                                        Project.status == 26).paginate(page=page, per_page=per_page, error_out=False)
        return render_template('workList/to_be_seen.html', paginate=paginate)


@wkl.route('/check/', methods=['POST', 'GET'])  # 查看工作
@login_required
def check():
    pid = request.args.get('pid', 0)
    if pid == 0:
        return redirect(url_for('workListView.to_be_revised'))

    status = request.args.get('status', 0)
    project = Project.query.get(pid)
    if status > 0:
        project.status = status
        db.session.commit()
        return redirect(url_for('workListView.to_be_revised'))

    if request.method == 'GET':
        histories = History.query.filter(History.pid == pid)
        flag = histories.count()
        return render_template('workList/check.html', project=project, histories=histories, flag=flag)

    status = int(request.form.get('status'))
    if status == 27:
        project.status = status
        db.session.commit()
    return redirect(url_for('workListView.to_be_revised'))


@wkl.route('/completed/', methods=['GET'])  # 已完成工作
@login_required
def completed():
    uid = session.get('user')
    page = int(request.args.get('page', 1))

    if request.method == 'GET':
        paginate = Project.query.filter(Project.uid == uid,
                                        Project.status.in_([25, 27])).paginate(page=page, per_page=per_page, error_out=False)
        return render_template('workList/completed.html', paginate=paginate)


@wkl.route('/detail/', methods=['GET'])  # 已完成工作内容
@login_required
def detail():
    pid = request.args.get('pid', 0)
    if pid == 0:
        return redirect(url_for('workListView.to_be_revised'))

    if request.method == 'GET':
        project = Project.query.get(pid)
        histories = History.query.filter(History.pid == pid)
        flag = histories.count()
        return render_template('workList/detail.html', project=project, flag=flag, histories=histories)


@wkl.app_template_filter('dictFilter')
def dictFilter(num):
    return Dictionary.query.filter(Dictionary.pid == int(num)).first().name


@wkl.app_template_filter('userName')
def userName(num):
    return User.query.get(int(num)).uname

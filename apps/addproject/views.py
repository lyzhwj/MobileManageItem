import re

from flask import render_template, request, redirect, session

from apps.addproject import addproject
from apps.decorate import login_required
from apps.model import Project, db, Dictionary, Province, Officer


@addproject.route('/addproject/', methods=("GET", "POST"))
@login_required
def AddProject():
    # GET请求

    if request.method == "GET":
        pid = request.args.get('pid')
        print(pid)
        if pid:
            project = Project.query.filter(Project.id == pid).first()
            officer = Officer.query.filter(Officer.pid == pid).all()
            project.pre_ini_date = str(project.pre_ini_date).split(' ')[0]
            project.pre_end_date = str(project.pre_end_date).split(' ')[0]
            project.rea_ini_date = str(project.rea_ini_date).split(' ')[0]
            project.rea_end_date = str(project.rea_end_date).split(' ')[0]
            return render_template('addproject.html', project=project, officer=officer, pid=pid)

        p_num = Dictionary.query.filter(Dictionary.pid < 13).all()
        provinces = Province.query.filter().all()
        return render_template('addproject.html', p_num=p_num, provinces=provinces)

    # POST请求
    if request.method == "POST":
        pid = request.args.get('pid', 0)
        officers = request.form.get("officers")  # 审批人
        cls = request.form.get("cls")  # 项目类别
        pre_ini_date = request.form.get("pre_ini_date")
        rea_ini_date = request.form.get("rea_ini_date")
        total_account = float(request.form.get("total_account"))
        pro_name = request.form.get("pro_name")
        province = request.form.get("province")
        tel = request.form.get("tel")
        info = request.form.get("info")
        pre_end_date = request.form.get("pre_end_date")
        rea_end_date = request.form.get("rea_end_date")
        if pid:
            project = Project.query.get(pid)
            project.cls = cls
            project.pre_ini_date = pre_ini_date
            project.rea_ini_date = rea_ini_date
            project.total_account = total_account
            project.pname = pro_name
            project.province = province
            project.tel = tel
            project.info = info
            project.pre_end_date = pre_end_date
            project.rea_end_date = rea_end_date
            print(pid)
            print(project.pname)
            db.session.commit()
            return redirect('/planlist/')
        context = {
            "officers": officers,
            # "num": num,
            "cls": cls,
            "pre_ini_date": pre_ini_date,
            "rea_ini_date": rea_ini_date,
            "total_account": total_account,
            "pro_name": pro_name,
            "province": province,
            "tel": tel,
            "pre_end_date": pre_end_date,
            "rea_end_date": rea_end_date,
        }
        if re.match(r'^1[3|4|5|7||9|][0-9]{9}$', tel):
            return render_template('addproject.html', errmsg='手机格式错误')
        if all(context.values()):
            user = session.get('user')
            print(user)
            project = Project(pname=pro_name, catgory=cls, uid=user, tel=tel, province=province,
                              total_account=total_account, pre_ini_date=pre_ini_date, rea_ini_date=rea_ini_date,
                              pre_end_date=pre_end_date, rea_end_date=rea_end_date, info=info, status=21)
            db.session.add(project)
            db.session.commit()

            # 插入审批人数据
            officers_id = officers.replace(' ', '').split(';')
            for i in officers_id:
                officer = Officer(pid=project.id, uid=i)
                db.session.add(officer)
                db.session.commit()

        else:
            msg = "信息不全"
            return msg

    return redirect('/planlist/')


@addproject.route('/planlist/')
def PlanList():
    pid = request.args.get('pid')
    user = session.get('user')
    project = Project.query.filter(Project.uid == user).all()
    officer = Officer.query.filter(Officer.pid == project[0].id).all()
    print(project[0].status)
    if pid:
        Project.query.filter(Project.id == pid).first().status = 22
        db.session.commit()
    return render_template('planlist.html', project=project, officer=officer)

import re

from flask import render_template, request

from apps.addproject import addproject
from apps.model import Project, db, Dictionary, Province, Officer


@addproject.route('/addproject/', methods=("GET", "POST"))
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
            return render_template('addproject.html',project=project, officer=officer)

        p_num = Dictionary.query.filter(Dictionary.pid < 13).all()
        provinces = Province.query.filter().all()
        return render_template('addproject.html', p_num=p_num, provinces=provinces)
    # POST请求
    if request.method == "POST":
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
        msg = "1"
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
            project = Project(pname=pro_name, catgory=cls, uid=1, tel=tel, province=province,
                              total_account=total_account, pre_ini_date=pre_ini_date, rea_ini_date=rea_ini_date,
                              pre_end_date=pre_end_date, rea_end_date=rea_end_date, info=info)
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

    return "提交成功"


@addproject.route('/planlist/')
def PlanList():
    project = Project.query.filter(Project.uid == 1).all()
    print(project[0].id)
    officer = Officer.query.filter(Officer.pid == project[0].id).all()

    return render_template('planlist.html', project=project, officer=officer)

from flask import render_template, request

from apps.addproject import addproject
from apps.model import Project

@addproject.route('/addproject/', methods=("GET", "POST"))
def AddProject():
    # GET请求
    if request.method == "GET":
        return render_template('addproject.html')
    # POST请求
    if request.method == "POST":
        principal = request.form.get("principal")
        num = request.form.get("num")
        cls = request.form.get("cls")
        pre_ini_data = request.form.get("pre_ini_data")
        rea_ini_data = request.form.get("rea_ini_data")
        total_account = request.form.get("total_account")
        pro_name = request.form.get("pro_name")
        provinces = request.form.get("provinces")
        tel = request.form.get("tel")
        pre_end_data_ = request.form.get("pre_end_data")
        rea_end_data = request.form.get("rea_end_data")
        msg = "1"
        context = {
            "principal": principal,
            "num": num,
            "cls": cls,
            "pre_ini_data": pre_ini_data,
            "rea_ini_data": rea_ini_data,
            "total_account": total_account,
            "pro_name": pro_name,
            "provinces": provinces,
            "tel": tel,
            "pre_end_data_": pre_end_data_,
            "rea_end_data": rea_end_data,


        }

        if all(context.values()):


           pass
        else:
           msg="信息不全"
           return msg

    return "提交成功"


@addproject.route('/planlist/')
def PlanList():
    return render_template('planlist.html')

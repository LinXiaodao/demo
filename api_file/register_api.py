# -*- coding: utf-8 -*-
from flask import request
from api_file.login_register import UserLoginRegister

# 接口注册
def register_fuc(app,addr,port):
    user_Instance = UserLoginRegister(addr,port)
    #首页
    @app.route('/',methods=['GET','POST'])
    def home_service():
        res = user_Instance.home()
        return res

    @app.route('/userRegister',methods=['POST'])
    def user_register_service():
        params = request.form.to_dict() #获取请求参数
        res = user_Instance.user_register(params)
        return res

    @app.route('/userLogin',methods=['POST'])
    def user_login_service():
        params = request.form.to_dict()   
        res = user_Instance.user_login(params)
        return res

    @app.route('/upload',methods=['GET','POST'])
    def upload_service():
            
# -*- coding: utf-8 -*-
from flask import Flask
import api_file.register_api as get_user
import os
import pymongo
from base.data import Base
#注册服务
# class Base():
#     def __init__(self,addr,port):
#         self.addr = addr
#         self.port = port


class RunApp():
    def __init__(self,addr,port):
        Base(addr,port)
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = os.urandom(24) # 随机产生24位的字符串作为SECRET_KEY,每次服务启动会变
        self.register_service(self.app,addr,port)
        self.app.run(debug=True) 

    #注册接口
    def register_service(self,app,addr,port):
        get_user.register_fuc(app,addr,port)
#开启服务
RunApp('localhost',27017)
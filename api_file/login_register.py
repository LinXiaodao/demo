# -*- coding: utf-8 -*-
from flask import render_template,request
from base.data import Base
from base.common import connet_database,encrypt_data
import requests
import uuid
import json
class UserLoginRegister(Base):
    def home(self):
        def getdate(db):
            cols = db['users']
            print(list(cols.find({})[:]),'获取用户数据')
        connet_database(self.addr,self.port,'admin',getdate)
        return render_template('index.html')
    
    def user_register(self,params):
        res = {}
        def getdate(db):
            nonlocal params
            cols = db['users']
            user_mes = {
                'id': str(uuid.uuid1()),
                'name': params['name'],
                'password':encrypt_data(params['password']),
                'email':params['email'],
            }
            insert_result = cols.insert_one(user_mes)
            if not insert_result.inserted_id is None:
                res['desc'] = '新增成功'
            else:
                res['desc'] = '新增失败'
        connet_database(self.addr,self.port,'admin',getdate)
        return json.dumps(res,ensure_ascii=False)

    def user_login(self,params):
        res = {}
        def getdate(db):
            nonlocal res
            cols = db['users']
            user_mes = {
                'name':params['name'],
                'password':encrypt_data(params['password'])
            }
            find_result = list(cols.find({'name':user_mes['name']})[:])
            if len(find_result)>0:
                if find_result[0]['password'] == user_mes['password']:
                    res['desc'] = '登录成功'
                else:
                    res['desc'] = '账号或密码错误，请重新输入'
            else:
                res['desc'] = '用户不存在，请重新输入'
        connet_database(self.addr,self.port,'admin',getdate)
        return json.dumps(res,ensure_ascii=False)
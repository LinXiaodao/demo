# from wsgiref.simple_server import make_server

# from backstage import application

# httpd = make_server('',8080,application)
# print('服务开启，正在监听8080端口：')

# httpd.serve_forever()

from flask import Flask,request,render_template
import json
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

#标识条件查询接口
@app.route('/analysisHandleName',methods=['POST'])
def get_analysis_handle_name():
    identification = request.form.to_dict()
    res = requests.get('http://idisif.gdsinsing.com:8080/88.168.88/SM018-1520') #查询
    return json.dumps(res.json(),ensure_ascii=False)
#标识条件查询接口-index
@app.route('/analysisByIndex',methods=['POST'])
def get_analysis_index():
    identification = request.form.to_dict()
    params = {
        'action':'query',
        'index':identification['index']
    }
    res = requests.post('http://idisif.gdsinsing.com:8080/'+identification['identification'],data = json.dumps(params)) #查询
    print(res.request.body,'发送报文')
    return json.dumps(res.json(),ensure_ascii=False)

#创建标识
@app.route('/addIdentification',methods=['POST'])
def addIdentification_server():
    identification = request.form.to_dict()
    params = {
        'value':[{
            'index':identification['index'],
            'type':identification['type'],
            'data':{
                'format':'string',
                'value': '{"itemName":"产品图片","itemClass":"CPSM","itemValue":"/home/image/88.168.88/SM018-1520/chuangdian_SM018.jpg"}'
            }
        },
        ]
        
    }
    res = requests.post('http://idisif.gdsinsing.com:8080/'+identification['identification'],data=json.dumps(params)) #查询
    print(res.request.body,'发送报文')
    return json.dumps(res.json(),ensure_ascii=False)
#删除标识
@app.route('/delIdentification',methods=['POST'])
def delIdentification_server():
    identification = request.form.to_dict()
    res = requests.delete('http://idisif.gdsinsing.com:8080/'+identification['identification'])
    return json.dumps(res.json(),ensure_ascii=False)

#创建标识值
@app.route('/addIdentificationIndex',methods=['POST'])
def addIdentificationIndex_server():
    identification = request.form.to_dict()
    params = {
        "action": "addHandleValue",
        'value':[{
            'index':identification['index'],
            'type':identification['type'],
            'data':{
                'format':'string',
                'value': '{"itemName":"产品图片","itemClass":"CPSM","itemValue":"/home/image/88.168.88/SM018-1520/chuangdian_SM018.jpg"}'
            }
        }]
    }
    res = requests.put('http://idisif.gdsinsing.com:8080/'+identification['identification'],data=json.dumps(params))
    print(res.request.body,'发送报文')
    return json.dumps(res.json(),ensure_ascii=False)

#标识值删除接口
@app.route('/delIdentificationIndex',methods=['POST'])
def delIdentificationIndex_server():
    identification = request.form.to_dict()
    params = {
        "action":"removeHandleValue", 
        "index":[identification['index']]
    }
    res = requests.put('http://idisif.gdsinsing.com:8080/'+identification['identification'],data=json.dumps(params))
    print(res.request.body,'发送报文')
    return json.dumps(res.json(),ensure_ascii=False)

#标识值修改接口
@app.route('/updateIdentificationIndex',methods=['POST'])
def updateIdentificationIndex_server():
    identification = request.form.to_dict()
    params = {
        "action":"modifyHandleValue", 
        'value':[
            {
                "index":identification['index'],
                'type':identification['type'],
                'data':{
                    'format':'string',
                    'value': identification['value']
                }                
            }
        ]

    }
    res = requests.put('http://idisif.gdsinsing.com:8080/'+identification['identification'],data=json.dumps(params))
    print(res.request.body,'发送报文')
    return json.dumps(res.json(),ensure_ascii=False)


if __name__ == '__main__':
    app.run(port='8090',debug=True)

 

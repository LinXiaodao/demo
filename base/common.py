import pymongo
import hashlib

#连接数据库
def connet_database(db_addr,db_port,db_name,callback):
    client = pymongo.MongoClient(db_addr,db_port)
    db = client[db_name]
    callback(db)
    client.close()

#数据加密
def encrypt_data(data):
    h = hashlib.sha256()
    h.update(bytes(data,encoding='utf-8'))
    return h.hexdigest()
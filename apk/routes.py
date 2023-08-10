from datetime import datetime
import datetime
import json
from flask import request
import requests
from sqlalchemy import inspect, select
from apk.models import Users
from app import app,db

@app.route('/users/fetch',methods=['GET','POST'])
def fetch_data():
    url=('https://reqres.in/api/users')
    response=requests.get(url)
    data=json.loads(response.text)
    page=request.args.get('page')
    if page=='1':
        var=data['data']
        for i in var:
           check= select(Users).where(Users.id==i['id'])
           rsp=db.session.execute(check)
           response=rsp.scalar_one_or_none()
           if response is None:
                user= Users(id=i['id'],avatar=i['avatar'],email=i['email'],first_name=i['first_name'],last_name=i['last_name'],created_at=datetime.now())
                db.session.add(user)
                db.session.commit()
           else:
               raise ValueError('Already Exists')
    else:
        raise ValueError('no page')
    return var
def object_as_dict(obj):
    return{c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")
  
@app.route('/get_users')
def get_data():
    query= select(Users)
    rsp=db.session.execute(query)
    data=rsp.scalars().all()
    b=[]
    for i in data:
        a=object_as_dict(i)
        b.append(a)
    return json.dumps(b,default=serialize_datetime)

@app.route('/get_users/<id>',methods=['GET'])
def get_data_id(id):
    query=select(Users).where(Users.id==id)
    rsp=db.session.execute(query)
    data=rsp.scalar_one_or_none()
    var=object_as_dict(data)
    return json.dumps(var,default=serialize_datetime)

@app.route('/create_users',methods=['POST'])
def create_data():
  
   if request.method == 'POST':
        form = request.json
        users=Users(**form)
        db.session.add(users)
        db.session.commit()
        var=object_as_dict(users)
        return json.dumps(var,default=serialize_datetime)

@app.route('/update_users/<id>',methods=['PUT'])
def update_data(id):
    query=select(Users).where(Users.id==id)
    rsp=db.session.execute(query)
    data=rsp.scalar_one_or_none()
    if data is not None:
        form=request.json
        users=Users(**form)
        data.first_name=users.first_name
        data.last_name=users.last_name
        data.avatar=users.avatar
        data.email=users.email
        data.updated_at=users.updated_at
        db.session.add(data)
        db.session.commit()
        var=object_as_dict(data)
        return json.dumps(var,default=serialize_datetime)
@app.route('/delete_users/<id>',methods=['DELETE'])
def delete_data(id):
    query=select(Users).where(Users.id==id)
    rsp=db.session.execute(query)
    data=rsp.scalar_one_or_none()
    headers=request.headers.environ['HTTP_AUTHORIZATION']
    token=headers.split(' ')
    if data is not None and token[1]=='3cdcdnTiBsl':
        db.session.delete(data)
        db.session.commit()
        var=object_as_dict(data)
        return json.dumps(var,default=serialize_datetime)
    else:
        raise ValueError('Data Not Found or Headers Token not Same')
        
        

    

    

    

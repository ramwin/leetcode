import json

import peewee

db = peewee.MySQLDatabase(
    "wangx",
    user="wangx",
    password=input("输入数据库密码: "),
)


class User(peewee.Model):

    Users_Id = peewee.AutoField()
    Banned = peewee.CharField()
    Role = peewee.CharField()

    class Meta:
        table_name = "Users"
        database = db


class Trips(peewee.Model):
    Id = peewee.AutoField()
    Client_Id = peewee.IntegerField()
    Driver_Id = peewee.IntegerField()
    City_Id = peewee.IntegerField()
    Status = peewee.CharField()
    Request_at = peewee.DateField()

    class Meta:
        table_name = "Trips"
        database = db


f = open("行程和用户.json")
data = json.load(f)
[i.delete_instance() for i in Trips.filter()]
[i.delete_instance() for i in User.filter()]
for user in data["rows"]["Users"]:
    User.create(
        Users_Id=user[0],
        Banned=user[1],
        Role=user[2],
    )
for trip in data["rows"]["Trips"]:
    Trips.create(
        Id=trip[0],
        Client_Id=trip[1],
        Driver_Id=trip[2],
        City_Id=trip[3],
        Status=trip[4],
        Request_at=trip[5],
    )

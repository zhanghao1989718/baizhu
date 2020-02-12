# coding:utf-8
import pymysql

# 创建一个person表
db = pymysql.Connect(
  host='baizhudata.mysql.rds.aliyuncs.com',port=3900,
  user='intelsys',passwd='Baizhu7958',database='intelsys')
#创建一个游标
cursor = db.cursor()
# 创建表
sql = '''
CREATE TABLE `test_get_data` (
  `id` int(15) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `sid` char(20) NOT NULL,
  `soft_name` char(20) NOT NULL,
  `num` int(11) NULL,
  `return_point` double(14,3) NULL,
  `price` double(14,3) NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE INDEX (`date`,`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8
'''

# 编写插入数据的sql
# sql = "replace into test_get_data (date,sid,soft_name,num,return_point,price) values (%s, %s, %s, %s, %s, %s)"

# 用ID做了排重写法
# sql = "replace into test_get_data (id,date,sid,soft_name,num,return_point,price) values (%s, %s, %s, %s, %s, %s, %s)" \
#       "on duplicate key update num=values(num), return_point=values(return_point), price=values(price)"

cursor.execute(sql)
cursor.close()
db.close()
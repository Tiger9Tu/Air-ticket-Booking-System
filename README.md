# Air-ticket-Booking-System

# 飞机订票系统-后端框架



## 环境

数据库：opengauss-Docker

后端框架：Django 3.2.13（更高版本不支持opengauss）

操作系统：win10/11

### 配置方法

1.数据库（参照[node.js连接openGauss-云社区-华为云 (huaweicloud.com)](https://bbs.huaweicloud.com/blogs/detail/296774)）

```
docker pull enmotech/opengauss

docker run --name opengauss --privileged=true -d -e GS_PASSWORD=Huawei@123A -p 15432:5432 enmotech/opengauss:latest -v pgVol:/var/lib/opengauss

docker exec -it <container id> /bin/bash

create user wuyicom with password 'Huawei@123';

create database testdb owner wuyicom;

GRANT ALL PRIVILEGES ON DATABASE testdb to wuyicom;

GRANT ALL PRIVILEGES TO wuyicom;

ALTER ROLE wuyicom CREATEDB;
```



2.后端框架

```
// 开启python虚拟环境
python -m venv pyvenv
cd pyvenv/Scripts
activate.bat
// 下载框架（django）和opengauss驱动（psycopg2）
pip install django=3.2.13
pip install psycopg2

//后面的命令见Django
```



## 参考资料

[opengauss-考试系统](https://blog.csdn.net/weixin_45816954/article/details/124183612)

[Django文档](https://docs.djangoproject.com/zh-hans/4.1/intro/tutorial01/)

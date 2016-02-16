# django-rest-framework-tutorial
Django-Rest-Framework 教程



----------
## version 7.0 ##

Django-Rest-Framework 教程: 6. ViewSets 和 Routers

[http://www.weiguda.com/blog/24/](http://www.weiguda.com/blog/24/)


参考：

[https://github.com/CoderDream/rest-framework-tutorial](https://github.com/CoderDream/rest-framework-tutorial)




----------
## version 6.0 ##

Django-Rest-Framework 教程: 5. 提高关联性和超链接API


![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v6.0/v060001.png)



----------
## version 5.0 ##
Django-Rest-Framework 教程: 4. 验证和权限

[http://www.weiguda.com/blog/22/](http://www.weiguda.com/blog/22/)

curl -X POST http://127.0.0.1:8000/snippets/ -d "code=print 789" -u xulin:1234

![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v5.0/v050001.png)

----------
## version 4.0 ##
Django-Rest-Framework 教程: 3. 使用 class based views

[http://www.weiguda.com/blog/21/](http://www.weiguda.com/blog/21/)



----------
## version 3.0 ##
Django-Rest-Framework 教程: 2. Requests 和 Responses
[http://www.weiguda.com/blog/20/](http://www.weiguda.com/blog/20/)


curl -H 'Accept: application/json; indent=4' -u xulin:1234 http://127.0.0.1:8000/snippets/


![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v3.0/v030001.png)


使用Accept头部信息控制response返回格式:

    curl -u xulin:1234 http://127.0.0.1:8000/snippets/ -H 'Accept: application/json'  # JSON
    curl -u xulin:1234 http://127.0.0.1:8000/snippets/ -H 'Accept: text/html'         # HTML
或者使用后缀控制返回格式:

    curl -u xulin:1234 http://127.0.0.1:8000/snippets/.json  # JSON suffix
    curl -u xulin:1234 http://127.0.0.1:8000/snippets/.api   # Browsable API suffix
通过修改request的Content-Type头部, 控制格式:

    # 使用form data POST
    curl -X POST -u xulin:1234 http://127.0.0.1:8000/snippets/ -d "code=print 123"

    {"id": 3, "title": "", "code": "print 123", "linenos": false, "language": "python", "style": "friendly"}

    # 使用JSON POST
    curl -X POST -u xulin:1234 http://127.0.0.1:8000/snippets/ -d '{"code": "print 456"}' -H "Content-Type: application/json"

    {"id": 4, "title": "", "code": "print 456", "linenos": true, "language": "python", "style": "friendly"}



----------
## version 2.0 ##

Django-Rest-Framework 教程: 1. 序列化 (Serialization)




![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v2.0/v020001.jpg)


----------
## version 1.0 ##

Django-Rest-Framework 教程: 快速入门

[http://www.weiguda.com/blog/18/](http://www.weiguda.com/blog/18/)

环境准备

1, 先安装virtualenv
	
> pip install virtualenv

2, 在需要安装虚拟环境的工程目录下设置env环境
> virtualenv env

3, 激活env环境
> env\scripts\activate

4, 然后运行安装命令：

> pip install -r requirements/local.txt

5, 在eclipse中设置环境
	![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v1.0/v010007.png)


6, 在项目中设置环境
	![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v1.0/v010008.png)



通过curl命令访问

![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v1.0/v010001.jpg)



通过浏览器访问：

1. 首页：

	![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v1.0/v010002.jpg)

2. 使用创建数据库时的用户名密码登录:

	![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v1.0/v010003.jpg)

3. 进入页面后可以看到相关的URL

	![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v1.0/v010004.jpg)

4. 进入用户列表页面：

	![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v1.0/v010005.jpg)

5. 进入群组列表页面：

	![](https://raw.githubusercontent.com/CoderDream/django-rest-framework-tutorial/master/docs/snapshot/v1.0/v010006.jpg)


----------
Django初始化数据库


initial_data.json

1. 导出数据到json：
	dumpdata app > data.json

2. 初始数据：
	将json数据放到app\fixtures\文件夹下

----------

Windows下安装mysql-python(MySQLdb)诺干问题及解决方

http://cyfloel0516.sinaapp.com/?p=193

解决办法：最最最无耻的解决办法，由于在Virtualenv下安装包确实会出现各种古里古怪的问题，因此，只有一个最终的绝招了。拿Mysql-python为例。Mysql-python的制作者估计知道windows下安装有多么的困难，因此，在Windows下有提供exe安装包，下载地址。下载完成后，安装。由于这个安装包只读取注册表下的Python安装目录，因此，安装目标是我们本机的Python环境，而不是Virtualenv的安装环境，怎么解决呢？其实很简单，安装完毕后，找到本机的Python安装目录下的包目录，以我本机为例：C:\Python27\Lib\site-packages。在这个目录下找到Mysql相关的文件及文件夹，一共有6个：

MySQL_python-1.2.3-py2.7.egg-info(文件夹)
MySQLdb(文件夹)
_mysql.pyd
_mysql_exceptions.py
_mysql_exceptions.pyc
_mysql_exceptions.pyo
将这些文件及文件夹复制到Virtualenv所创建的沙盒的Lib\site-packages文件夹下即可。这种方法在目前的使用中，我还没发现有什么问题。




----------




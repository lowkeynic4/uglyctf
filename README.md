简介：
在!(ctfmanager)[https://github.com/pdogg/ctfmanager]基础上修改而来。
支持用户注册，支持多个比赛，支持赛时设置，支持查看所有人比分，使用sqlite数据库因为移动时方便。
有注册码功能，但是需要手动添加注册码
使用方法

1. 下载django1.8.4 下载bootstrap-admin
2. 运行之前先创建数据库python manage.py migrate
3. 创建管理员 python manage.py createsuperuser
4. 转到url:<YOUR URL>/admin/ 登陆
* 然后先创建一个Game
* 创建一个Categories
* 创建一个Chanllenges


TO-DO list:
* 在提交key时增加延迟，防止爆破
* 增加检验和警告功能防止过分提交错误的flag，现在是通过管理员手工设置
* 添加上传文件功能，因为有写题目需要给出文件就可以答题了




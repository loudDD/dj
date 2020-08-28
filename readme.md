pycharm导入db需要下载插件
django-admin startproject xx
python manage.py startapp xx
python manage.py shell 类似ipython，直接显示结果
MVT：
	model:连接数据库，使用面向的对象的方式，来处理
	view: 视图（控制器），接收请求，处理数据，返回响应
	template:html，css,js等html模板文件	 ，视图返回请求前，通过出入处理后的数据到template文件渲染后，进行响应
# template: 
	html文件模板
	文件需要在setting.py  templates中注册，3.1自动添加路径
# url: 
	路由 即路径 localhost:8000/  之后的路径
	path("pa",views.func)
	localhost：8000/pa  内容：func返回的内容
	多个app的views需要导入时
	from xx import views as xxx 进行重命名
	无法导入相同模块名
	可有多个urls.py  项目和app都可以有，依次从项目的urls开始匹配，app的urls需要再项目的urls传入

# views： 
	控制器， 进行数据处理等，即返回数据
	1.传入数据到template中，渲染后，用户通过路径访问
	2.render(request,"pagename.html,context)
	3.直接返回内容用HttpResponse("")
	4 context 字典，可传入参数到html，html使用参数 {{字典key}}

# model: ORM
## 数据类型
	1.连接数据库，默认自带的sqlite
	2.类 -- 表  属性 -- 字段
	3.继承models.Model,格式一般为大写开头，Field结尾；内部要求 需了解
		3.1 主键id自动生成 
		3.2 外键需添加外键对象
		3.3 属性名就是字段名
	```
	class people(models.Model):
		name = models.CharField()
		
	```
	4. python manage.py makemigrations 创建关系 ，可在 migrations文件夹查看，进行操作等
	5. python manage.py migrate 进行迁移，自动创建表完成
	6. verbose_name admin后台显示的分栏名	
	7. models.CharFiled(max_lenght)必须有最大长度
	8. 可选属性null=True，是否可为为空；unique=False;整形和布尔类型，default=xx；
	9. 默认生成的表名：app名_model类名(小写) book_bookinfo
	10.自定义表名，model文件中的表类中中创建内部类
	```
	class bookInfo:
	
		class Meta:
			db_table= tablename
			verbose_name = '' #修改admin后台显示的名字
	
	```
	11. 枚举类型:理论上为有序字典；python字典为无序，所以使用二维元祖
	```
	gender_choice = ((0,'male'),(1,'femail'))
	gender = models.SmallIntegerField(choices=gender_choice,default=0)
	```
	12.外键 ON_DELETE = models.CASCADE
		1.CASCADE 删除主表的时候，从表数据也删掉
		2.PROTECT 无法删除主表字段时
		3.SET_NULL 主表字段删除后，不影响从表，从表相关字段变为null
## 数据库
修改为mysql
1.pip install PyMySQL
2.django同名子目录的__init__.py中写入
```
import pymysql
pymysql.install_as_MySQLdb()
```
3.修改setting.py
```
DATABSES= {
	default:{
	'ENGINE':'django.db.backends.mysql',
	'HOST':'',
	'PORT':'',
	'USER':'',
	'PASSWORD':'',
	'NAME':'database_name',#已有
		}
	}
```
4.进行迁移

# setting.py
	INSTALLED_APPS 中进行app的注册，可使用包名或包.apps.类名
# model数据	
## 创建超级用户，管理数据
	1.地址 ip/admin
	2.python manage.py createsuperuser
	3.需要再项目admin中注册要修改的models
		admin.site.register(book.models.BookInfo)
	4.修改admin中数据显示
		重写BookInfo中的__str__
## view中处理使用数据
	1. 在view中导入 from book.models import BookInfo
	2.books = BookInfo.objects.all()
	3. context = {'books':books}
	4.return render(request,'index.html,context)
	html中传入数据,通过{{key.字段名}}访问，如果重写了__str__，也可以直接用{{key}}，返回的是__str__中的返回值
	<ul>
		{%for book in books%}
		<li>{{book.name}}</li>
		{#endfor %}
	</ul>
# 文件
## 静态文件
### STATIC_URL ='/static/' 当访问路径为ip+port+STATIC_URL+filename django将访问静态文件,否则视为动态文件，根据路由进行匹配
STATICFILES_DIRS=[os.path.join(BASE_DIR,'images'),] 静态文件路径为STATICFILES_DIRS中的路径
### 一般静态文件放在根目录的static文件夹中

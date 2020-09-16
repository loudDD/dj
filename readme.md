pycharm导入db需要下载插件
django-admin startproject xx
python manage.py startapp xx
python manage.py shell 类似ipython，直接显示结果

python manage.py runserver 0.0.0.0:8000 所有局域网内可以访问

# MVT：
	model:连接数据库，使用面向的对象的方式，来处理
	view: 视图（控制器），接收请求，处理数据，返回响应
	template:html，css,js等html模板文件	 ，视图返回请求前，通过出入处理后的数据到template文件渲染后，进行响应
# template: x
	html文件模板
	文件需要在setting.py  templates中注册，3.1自动添加路径
# url: 
	路由 即路径 localhost:8000/  之后的路径
	path("pa",views.func)
	localhost：8000/pa  内容：func返回的内容
	多个app的views需要导入时
	from xx import views as xxx 进行重命名
	无法导入相同模块名
	可有多个urls.py  项目和app都可以有，依次从项目的urls开始匹配，app的urls需要在项目的urls传入
## 匹配顺序
- 没有最优匹配规则
```
path(r'^hehe',views.hehe),
path(r'^hehehe',views.hehehe)
当访问hehehe时，匹配到hehe就停止了，返回hehe
所以路径用/hehe/包括起来，甚至可以加 ^hehe$以hehe开头，hehe结尾
```
## 获取参数
- 通过url路径中的<类型:参数名>
- url返回的参数格式为str
- 每个<>都是一个参数，数量要对应

```python
path(r'^student/<int:id>/',views.student)
def student(request,id):
	#通过形参参数名获取url路径中的参数
	#参数变成str格式
	return HttpResponse(id , type(id))
```
## 状态码
### 异常状态
#### 手动抛出异常
``` Http404
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")
```
#### 自动抛出异常
- from django.shortcuts import  get_object_or_404
- get_object_or_404(model对象，条件)
```
question = get_object_or_404(Question, pk=question_id)
return render(request, "polls/datails.html", {question: question})
```
### 重定向
- 相对url '/vote/details
- 完整url ‘https://example.com’
- models对象
```python
def xxx(request):
	return redirect()
	
```
## URL 命名空间

- 为了分辨不同app重名的url

- 添加 urls.py添加 app_name = 'appname'

  ```
  app_name = 'polls'
  urlpatterns = []
  or
  根路由中
  urlpatterns = [
  path("demo/",includ('demo.urls'),app_name=" ")
  ]
  ```

- html中,viewname -> appname:viewname

  ```
  app_name=polls
  path('detail/<int:question_id>/',view.detail,name='detail')
  <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
  ```

  

# views： 

控制器， 进行数据处理等，即返回数据
- 传入数据到template中，渲染后，用户通过路径访问
- render(request,"pagename.html,context)
```
相当于 
page = loader.get_template('pagename.html')
result = page.render(context)
return HttpResponse(result)
```
- 直接返回内容用HttpResponse("")
- context 字典，可传入参数到html，html使用参数 {{字典key}}

# model: ORM
## 数据类型
	1.连接数据库，默认自带的sqlite
	2.类 -- 表  属性 -- 字段
	3.继承models.Model,字段格式一般为大写开头，Field结尾；内部要求 需了解
		3.1 主键id自动生成 
		3.2 外键需添加外键对象
		3.3 属性名就是字段名
	```
	class people(models.Model):
		name = models.CharField(db_column='数据库列名')
		
	```
	4. python manage.py makemigrations 创建关系 ，可在 migrations文件夹查看，进行操作等
	5. python manage.py migrate 进行迁移，自动创建表完成
	6. verbose_name admin后台显示的分栏名（也可直接在字段属性中添加改选项）	
	7. models.CharFiled(max_length)必须有最大长度
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
	gender_choice = ((0,'male'),(1,'fema'))
	gender = models.SmallIntegerField(choices=gender_choice,default=0)
	```
	12.外键 ON_DELETE = models.CASCADE
		1.CASCADE 删除主表的时候，从表数据也删掉
		2.PROTECT 无法删除主表字段时
		3.SET_NULL 主表字段删除后，不影响从表，从表相关字段变为null
	13. DateField 传入值格式为datetime
	    将str转换为datetiem datetime.strptime("2010-01-01" , "%Y-%m-%d")
	    DateField.auto_now = false(默认)

## 处理使用数据
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
## 插入数据
### 方式1
```
#返回新生成的对象，需手动调用save
book=BookInfo(
	name ='',
	xx=xx,
)
book.save()
book = BookInfo()
book.name = ''
book.save()
```
### 方式2
直接入库
```
# 通过objects可以直接进行所有增删改查操作,返回新生成的对象，无需调用save
BookInfo.objects.create(
	name = '',
	xx= '',
)
```
### 涉及外键

```

class Class_List(models.Model):

    c_name = models.CharField(max_length=100)

class Students(models.Model):

    s_name = models.CharField(max_length=30)
    s_class = models.ForeignKey(Class_List,on_delete=models.CASCADE)
```

1. 需先插入Class_List数据

2. 插入Students数据时，s_classid需等于Class_List的实例

   ```
          # Class_List.objects.create(c_name="classone")
       # Class_List.objects.create(c_name="classtwo")
       # Class_List.objects.create(c_name="class3")
       class1 = Class_List.objects.get(pk=1)
       class2 = Class_List.objects.get(pk=2)
       Students.objects.create(s_name="tom1",s_class=class1)
       Students.objects.create(s_name="jerry2",s_class=class1)
       Students.objects.create(s_name="lily3",s_class=class2)
   
   ```

   



## 查询数据

- get 返回一条数据的对象
- all 返回所有数据,类似列表,可以通过列表方式切片查询，不能为负
- count 返回数量
  BookInfo.objects.count()
  BookInfo.objects.all().count()

```
book = BookInfo.objects.get(id=1) #得到某条数据

book.属性名 #得到字段值
```
BookInfo.object.all().filter().values(字段值)#获取某（字段值）列的值
```
times = books.filter(pub_date__isnull=False).values("pub_date")
#返回字典{属性名：值}
time = [x['pub_date'].strftime('%Y-%m-%d ') for x in times] 
#返回2010-01-01

```
- first() 返回查询的第一个对象

- last()

- exists() 是否有数据，有则返回True

- 查询集

  ```
  classnumber = Student.objects.filter(class="1")
  students = classnumber.s_name_set.all
  级联查询时，如果返回的是一个列表，django会自动将结果变成一个结果set 字段__set，再通过set来遍历，获取每个元素的字段
  ```

  

### where

语法格式  关键字（属性名__条件=值）
#### 条件
```
会自动补齐
exact  等于
contains 包含
isnull 为空 =True/False
startswith
endswith
in   在...中
gt  大于 
gte 大于等于
iexact/iendswith/xxx 词首添加i，忽略大小写的匹配
```

1.filter 过滤
```
BookInfo.objects.get(id__exact=1)
BookInfo.objects.filter(id__exact=1)['name']
返回格式不同，filter可以通过列表取值方式取值
```
2.exclude 筛选后的结果



## 修改数据
### 方式1
```
#查询数据的objects.属性名，直接进行赋值;需手动调用save
book.objects.属性名=xx
book.save()
```
### 方式2
```
# 返回受影响的行数
book = BookInfo.objects.filter(id = 1).update(
	name = xx,
)
```
### 数据表内进行对比 F对象
进行数据字段间比较
from django.db.models import F
filter(字段名__条件=F('字段名'))
F('字段名')*2 可直接运算
### 多重条件 
1.filter().filter() == select x from x where xx and xx
2.filter(condition1,condition2)
3.Q对象
#### Q对象
```
from django.db.models import Q

or  Q() | Q()
and Q() & Q()
not ~Q()
filter(Q(id__gt=10) & Q())
```
#### pk
pk = primary key，用于条件查询 get(pk=1)
### 聚合函数
aggregate(聚合函数('字段名'))
```
from django.db.models import Sum,Avg,Max,Min,Count
BookInfo.objects.aggregate(sum('id'))
```
### 排序
默认升序
```
BookInfo.objects.all().order_by('readcount')
#降序 : -字段名
BookInfo.objects.all().order_by('-readcount')
```

## 删除数据
都不需要手动save,直接生效
### 方式1
```
BookInfo.objects.filter(id=1).delete()

```
### 方式2

```
book = BookInfo.objects.get(id=1)
book.delete()
```
## 数据异常捕获
```
try:
	BookInfo.objects.get(id=10)
except BookInfo.DoesNotExists:
	pass
```
## 数据库
修改为mysql
1.pip install PyMySQL
2.django同名子目录的__init__.py中写入
```
import pymysql
#pymysql.version_info = (1, 4, 13, "final", 0) django3.1.1需要添加
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
## INSTALLED_APPS 中进行app的注册，可使用包名或包.apps.类名	
## 静态文件
### STATIC_URL 
STATIC_URL ='/static/' 当访问路径为ip+port+STATIC_URL+filename django将访问静态文件,否则视为动态文件，根据路由进行匹配
### STATICFILES_DIRS
STATICFILES_DIRS=[os.path.join(BASE_DIR,'images'),] 静态文件路径为STATICFILES_DIRS中的路径
### 一般静态文件放在根目录的static文件夹中
### 其他参数
ALLOWED_HOSTS= ["*",] 所有可以访问到的ip都可以访问
LANGUAGE_CODE = ‘zh-Hans’
TIME_ZONE ='Asia/Shanghai

# model数据	
## 创建超级用户，管理数据
	1.地址 ip/admin
	2.python manage.py createsuperuser
	3.需要在项目admin中注册要修改的models
		admin.site.register(book.models.BookInfo)
	4.修改admin中数据显示
		重写BookInfo中的__str__
## 多级路由
- 二级路由内容和一级一样
- 需要在一级路由注册二级路由
    - path('re/', include('register.urls'))

# admin.py

```
from django.contrib import admin
from .models import Question
admin.site.register(Question)#添加question到管理页面，可以进行数据处理，相当于数据库的前段处理界面
```



# html

## 逻辑判断

### for

```
{%for x in xx %}
{% endfor %}
```

- 反向迭代 reversed

  ```
  {% for x in xx reversed %}
  ```

- 可对二元组，字典等进行解包

```
for x,y in xx
{{x}}{{y}}
```

- forloop

  - forloop.counter 从1开始计数

  - forloop.counter0 从0开始计数

  - forloop.revcounter 剩余数量，第一次为n，最后一次为1

  - forloop.revcounter0 剩余数量，第一次为n-1，最后一次为0

  - forloop.first 第一次遍历时，返回True

  - forloop.last最后一次遍历时，返回True

  - forloop.parentloop 嵌套循环式，父循环

    ```
    {% for country in countries %}
        <table>
        {% for city in country.city_list %}
            <tr>
            <td>Country #{{ forloop.parentloop.counter }}</td>
            <td>City #{{ forloop.counter }}</td>
            <td>{{ city }}</td>
            </tr>
        {% endfor %}
        </table>
    {% endfor %}
    
    ```

    

### if

```
{% if %}
{% elif %}
{% endif %}
```

- ifequal

  ```
  {% ifequal value1 value2%}
  ```


 - ifnotequal

    ```
    {% ifequal value1 value2%}
    ```

    

### 判空

- if

- empty标签

  ```
  {% empty %}
  	do
  {# 一般for为空时，进行判空处理#}
  ```

  

## 功能标签
### a标签
- {% url %}

- 最好在同级路由器配置好path('book/', bookview.getdata, name='book'),

- html中使用：
    ```html
    <a href="{% url  'book' book_id %}">book</a>
    可以为html地址，也可以用url中的name,可以进行传参
    #urls
    path('book/<int:book_id>/', views.book, name='book'),
    
    ```
### 过滤器
- 在变量显示前修改
```html
{{var | 过滤器}}
# 加法 add
{{p_age | add:5}}
# 减法（没有减法）
{{p_age | add:-5}}
# 大写 upper
{{p_age | upper}}
# 小写 lower
{{p_age | lower}}
# 连接 join
{{p_age | join "xx"}}
# 默认值 default
{{p_age | default value}}
# 时间装换为字符串date
{{date | date:'y-m-d'}}
# safe进行渲染（否则当成字符串）
{{p_age | safe}}
autoescapeon不进行渲染
autoescapeoff 进行渲染
{% autoescapeon %}
{% endautoescape%}
# 整除divisibleby
{% forloop.counter0|divisibleby:2 %}
```
## csrf

- django中用于跨站请求伪造保护

  ```
  {% csrf_token %}
  ```

  

### input

- type
  - text
  - password
  - submit
    - value 文字显示
- placeholde
  - 输入框默认显示

```
<input type=''
```

### form

```
<form action ="" >
	<input type='text' name = "">
</form>
```
- action 执行时，跳转的页面
	- 跳转的页面可以获取数据，request.POST.get(input's name)	
- method 请求方式
## 结构标签

### 继承extends
- 继承父模板的所有结构
```
不再使用html结构，直接{% extends 'xx.html' %}

```
- **同时，在子模板中无法再自由添加html代码，不生效，只能在既有的block中**
### 分块 block
```
{% block blockname%}
{% endblock %}
```
### include
```
{% include 'foot.html' %}
可以结合block使用
```
#### 继承的使用
- 先进行预设置
```
{% block content%}
	<h1>this is home</h1>
{% endblock %}
```
- 继承使用
```
{% extends 'home.html' %}

{% block content %}
    <h2>this is home one</h2>
{% endblock %}
```
- 覆盖之前的规划
	- 不想覆盖，而是覆写，可以添加 {{block.super}}，调用父类
	```
	{% block content %}
        {{ block.super }}
        <h2>this is home one</h2>
	{% endblock %}
	```
## 静态资源使用方法
```
模板中使用静态文件
#加载static设置
{% load static %}
#使用
{% static 'ralative path'%}
```

# 请求

- request.META
  - 打印请求所有信息

## get

- 当请求时，传入多对相同键参数
  - "http://127.0.0.1:8000/students/test?name=tom&name=jerry"
  - 会生成一个类字典结构数据，储存同一个键的所有值
  - 获取：request.GET.get(key)
    - 只返回最后一个结果
  - 全部获取request.GET.getlist(key)
    - 返回所有结果（列表形式）

# 响应

- content-type
  - 类似文件扩展名，不影响内容，为浏览器指引文件打开方式
  - MIME
  - 内容包括大类型和具体类型
    - text 大类型
    - html /plain具体类型

# 创建app全流程

1.django-admin start app xxx
2.settings.py 注册app
3.在models 中创建表，继承models.Model 
    python manage.py makemigrations
    python manage.py migrate
4.在template中创建html 使用或写入数据
5.views创建处理函数
def xx(request):
    return render(request,'xx.html',context)
6.
7.urls中注册路由，写入view

# objects 

- 默认生成

- 可以自己定义

- 关键字：models.Manager()

  ```python
  class Student(models.Model):
  	stuobject = models.Manager()#此时objects不会再生成
  ```

- 可以直接继承类，进行数据预处理

  ```
  class Student(models.Model):
  	stuobject = models.StudentManager()#此时objects不会再生成
  class StudentManager(models.Manager):
  	def get_queryset(self):
  		return 
  	deg create(self,a_name = ''):
      a =self.model()
      a.create()...
      super(AnimalManager.self).get_queryset().filter(is_delete=False)
  #objects.all就是返回get_queryset
  #对数据预处理，筛选  
  #调用 Student.StudentManager.all()
  ```

  

# 数据库外键

```
question = models.ForeignKey(Question,on_delete=models.CASCADE)
question 作为Question的主键
每个 question 都关联到一个 Question 对象
```


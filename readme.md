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



## URL 命名空间

- 反向解析，解除硬编码，通过appname:viewname定位

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

  ```- 
  app_name=polls
  path('detail/<int:question_id>/',view.detail,name='detail')
  <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
  ```

- 多级路由

  - 二级路由内容和一级一样
  - 需要在一级路由注册二级路由
    - path('re/', include('register.urls'))

# views： 

## 基础使用

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

  ## get

  - request.method =='get'
- request.GET.get('tag_property_name',defaultvalue_if_return_None)
  
  ## 扩展
  
  ### python中反向解析
  
	```
	from django.urls import reverse
  
  render(reverse("appname:viewname"))
  ```
  - 位置参数传参reverse('appname:viewname',args=(value1,))
  - 关键字参数reverse('appname:viewname',kwargs={})
    

# model: ORM
1.连接数据库，默认自带的sqlite
2.类 -- 表  属性 -- 字段
3.继承models.Model,字段格式一般为大写开头，Field结尾；内部要求 需了解
		3.1 主键id自动生成 
		3.2 外键需添加外键对象
		3.3 属性名就是字段名
	```
## 数据类型
### 字段
#### CharFiled
- 字符串
- max_length必须有最大长度
#### IntegerField
- 整型
- default 必须有默认值
#### BooleanField
- 布尔值
- default = True/False
#### DateTimeField
- auto_now 每次修改自动修改为当前时间
- auto_now_add 设置为创建时的时间
#### DateField
- auto_now 每次修改自动修改为当前时间
- auto_now_add 设置为创建时的时间
- datetime.date实例
```
	    将str转换为datetiem datetime.strptime("2010-01-01" , "%Y-%m-%d")
	    DateField.auto_now = false(默认)
```
#### SmallIntegerField
- 枚举类型:理论上为有序字典；python字典为无序，所以使用二维元祖
	```
	gender_choice = ((0,'male'),(1,'fema'))
	gender = models.SmallIntegerField(choices=gender_choice,default=0)
	```

#### ImageField

- upload_to='relative path' 
  - 路径不能以/开头	
  - 不用传文件名
  - 上传目的如有同名文件，自动重命名
  - 可以传入strftime支持的字段来自动生成路径，如%Y
- settings.py 中指定MEDIA_ROOT = ''
- settings.py中指定MEDIA_URL='/media/'
- 数据库中会存放相对于MEDIA_ROOT的相对路径
- ImageField的数据有url，path,delete等方法（img.objects.get().i_img.url）

#### ForeignKey

- models.ForeignKey(主表名，on_delete) 
- 外键 on_delete = models.CASCADE
##### CASCADE 
删除主表的时候，从表数据也删掉;从表数据无法直接删除
##### PROTECT 
主表有引用的时候，无法删除主表字段
##### SET_NULL 
主表字段删除后，不影响从表，从表相关字段变为null
### 通用字段属性
#### db_column 
字段中定义数据库中表名
#### verbose_name 
admin后台显示的分栏名（也可直接在字段属性中添加改选项）	
#### null=True
是否可为为空；
#### unique=False
整形和布尔类型
#### default
默认值
#### 表名
- 默认生成的表名：app名_model类名(小写) book_bookinfo
- 自定义表名
model文件中的表类中中创建内部类
```
class bookInfo:

class Meta:
db_table= tablename
verbose_name = '' #修改admin后台显示的名字

```
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
## 模型关系

- 主表：将主表的外键作为主键的表

- 从表：建立外键的表

- 谁声明关系，谁是从表

- 开发中，谁是主表

  - 如果必须删一个，留的是主表，删的是从表
  - 作为主键的是主表

### 1:1 

- 使用场景：复杂表拆解
- Django中OneToOneField
- on_field
- 实现
- 通过外键相似的OneToOneField实现，相当于ForeignKey中添加了unique=true
- 对外键添加了唯一约束（本来外键是N:1） 

### 1：N

- 通过ForeignKey实现
- 一个主表（mon）的数据，对应多个从表(children)的数据
- on_field
- related_name设置setname
- 主获取从：xx_set
- 从获取主：显示属性 主表.外键名

### M:N

- ManyToManyField
- 通过多个Foreignkey实现，创建对应关系，且对应关系uniqe=True,即外键不能同时相等
- 级联数据设置 从获取主与主获取从一样
	- add str （str）
	- remove
	- clear
	- set
	- 即使错误的数据操作，添加重复数据，删除不存在数据，不会报错
- 级联数据获取
	- 主获取从 从表名小写_set
```
person = Person.objects.last()
idcards = person.idcard_set.all()
```
	- 从获取主 主表.外键名
```
idcards = IDCard.objects.last()
persons = idcards.id_person.all()
```

- 
  - 从增加主  外键名.add
```
person = Person.objects.last()
idcard = IDCard.objects.last()
idcard.id_person.add(person)
idcard.save()
```
  - 主增加从  主表_set.add
```
person = Person.objects.first()
idcard = IDCard.objects.last()
person.idcard_set.add(idcard)
idcard.save()
```

### 默认属性：

#### CASCADE

- 从表删除，主表不受影响

- 主表删除，从表直接删除

#### PROTECT

- 为防止误操作，通常设置为此模式
- 主表如果存在级联数据，删除动作受保护，不能成功
- 想删，需要删除主表中所有级联数据
#### SET
- SET_NULL
- SET_DEFAULT 传入默认值
- SET()

### 级联数据获取
- 主获取从，隐形属性，默认就是级联模型的名字
- 从获取主，显性属性，就是属性的名字
- 其实只是有没有自动代码补充



## 继承

- 使用方法

```
class Animal(models.Model):
    a_name = models.CharField(max_length=10)

class dog(Animal):
    d_leg = models.CharField(max_length=20)

class cat(Animal):
    d_eat = models.CharField(max_length=20)

```

- 效果
  - Animal表正常
  - dog表的主键建立外键到Animal上
  - Animal的主键唯一，所以dog和cat的主键不是连续的
- 参数 abstract=True/False
  - 默认False，将通用字段（父类属性）放在父表中，特定字段放到子表中，中间使用外键连接
  - True时，抽象化，不再数据库产生映射，只继承父类的属性（即通用字段）不会生成父类表，通用字段+特定字段生成子表

```
class Animal(models.Model):
    a_name = models.CharField(max_length=10)
    class Meta():
    	abstract = True
```

## models -> sql

以上

## sql -> model

- python manage.py inspectdb 显示数据库中的表，且models中没有
- python manage.py inspectdb > app/models.py

```
class Book(models.Model):
    b_name = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Book'
```

- managed = False 表示此表不被迁移系统管理

## ForeignKey

- ForeignKey默认关联到主表的pk,但是on_field可以指定字段
- 默认related_name = 字段_set
- 外键添加关联是，需要的是从表实例，而不是具体对应的字段

```
class Person(models.Model):Z ., b   kk /Zz                          hhh
    p_name = models.CharField(max_length=16)
    p_sex = models.BooleanField(default=False)

class IDCard(models.Model):
    id_num = models.CharField(max_length=18,unique=True)
    id_person = models.OneToOneField(Person,null=True,blank = True , on_delete=models.CASCADE)
    
    def bind_card(request):
        person = Person.objects.last()
        idcard= IDCard.objects.last()
        idcard.id_person = person
        return HttpResponse('绑定成功')
```



## 数据异常捕获

```
try:
	BookInfo.objects.get(id=10)
except BookInfo.DoesNotExists:
	pass
```
## 引入数据库
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
## INSTALLED_APPS 

INSTALLED_APPS 中进行app的注册，可使用包名或包.apps.类名	

## 静态文件
### STATIC_URL 
STATIC_URL ='/static/' 当访问路径为ip+port+STATIC_URL+filename django将访问静态文件,否则视为动态文件，根据路由进行匹配
### STATICFILES_DIRS
STATICFILES_DIRS=[os.path.join(BASE_DIR,'images'),] 静态文件路径为STATICFILES_DIRS中的路径

一般静态文件放在根目录的static文件夹中

## MIDDLEWARE

导入中间件

## media
	### MEDIA_UTL

- settings.py 中指定MEDIA_URL='/media/'

- 字符串格式

  ### MEDIA_ROOT 

- settings.py中指定MEDIA_ROOT 

- 字符串格式

- 上传的路径是以MEDIA_ROOT/upload_to/
### urls.py
因为django服务器不服务media目录，所以需要额外在根路由添加
```
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 其他参数
ALLOWED_HOSTS= ["*",] ,且runserver 0.0.0.0:xx所有可以访问到的ip都可以访问,
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


# admin.py

```
from django.contrib import admin
from .models import Question
admin.site.register(Question)#添加question到管理页面，可以进行数据处理，相当于数据库的前段处理界面
```



# html

- 不同app的template中有同名的html
  - 在template中创建app同名的文件夹
  - 文件夹中创建html
  - views中引用时，'appname/htmlname.html'

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

#### 判空

- empty标签

  ```
  {% empty %}
  	do
  {# 一般for为空时，进行判空处理#}
  ```

    

### if

```
{% if %}
{% elif %}
{% else %}
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

    

  

## 模板标签
### url标签
- {% url %}

- 最好在同级路由器配置好path('book/', bookview.getdata, name='book')

- 传参

    - 变量直接传递变量名，不需要{{}}
    - 固定字符串，引号包括

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
<form action ="" method="" >
	<input type='text' name = "">
</form>
```
- action 执行时，跳转的页面
	- 跳转的页面可以获取数据，request.POST.get(input's name)	
- method 请求方式

#### 上传文件

1. 文件需要分成多个包进行上传，需要进行特殊的编码

```
form表头添加 enctype='multipart/form-data'
```

2. html中添加上传标签,input的类型为file

   ```html
   <form action='' method='post' enctyppe='multipart/form-data'>
   	<span>文件</span>
       <<input type='file name='zoluo.jpg'>  {# 上传操作#}
       <br>
       <input typpe='submit' value='上传'> {# 提交#}
   </form>
   ```

   

   

3. 文件储存在request.FILES属性中

```
views中获取文件
file = request.FILES.get(input_file_tag_name)
```

4. 写入，除txt等文本文件，需要二进制写入

```
with open(newfilepath,'wb') as f:
	for i in file.chunks(): #将文件变成块
		f.write(i)
		f.flush()
```

5. 可以配合数据库上传



### static

- 加载

```
{ % load static%} or {% staticfiles%}
```

- 使用

```
{% static 'relative_path'_to_static_dir%}
```

- 访问所有static文件

```
ip:port/static/filepath   127.0.0.1:8000/static/img/1.jpg
```

- 静态文件中的html不支持模板语言

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

## 属性

- content
- charset
- status_code

- content-type
  - 类似文件扩展名，不影响内容，为浏览器指引文件打开方式
  - MIME
  - 内容包括大类型和具体类型
    - text 大类型
    - html /plain具体类型

## 方法

- init 初始化

- write（）直接写初文件

  ```
  HttpsResponse().write()
  ```
 - flush() 冲刷缓冲区，

- set_cooke()
  ### JsonResponse

  - json
    - 主要内容
      - JsonObject
        - key:value
      - JsonArray
        - []
        - 普通数据类型或Json
      - JsonObject可以和JsonArray嵌套

  - 请求头内容自动返回content-type格式为application/json

    ```python
    data = {"name":“tom"}
    return JsonResponse(data=)
    # html
    {"name":“tom"}
    ```
## 状态码


question = get_object_or_404(Question, pk=question_id)
return render(request, "polls/datails.html", {question: question})
```
    ### 重定向

	- 参数 重定向的url

    #### 301
```
    HttpResonsePermanentRedirect() #状态码301，永久
    ```
    #### 302
    ```
    redirect = HttpResponseRedirect() #状态码302,临时
    ```

### 400
- HttpResponseBadRequest
#### 403
- HttpResponseForbidden 
#### 404
- HttpResponseNotFound
#### 405
- HttpResponseServerError
### Http404
### 手动抛出异常
``` Http404
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")
```
### 自动抛出异常
- from django.shortcuts import  get_object_or_404
- get_object_or_404(model对象，条件)


## 会话技术
### cookie

- 客户端会话技术
- 数据储存在客户端
- 键值对形式
- 默认cookie自动携带，本网站所有cookie
- 支持过期时间
- Cookie不能跨域名，跨网站

- 设置cookie,通过HttpResponse返回
```
HttpResponse().set_cookie('username', 'tom')
#html network
变成键值对形式的cookie
```
- 超时
	- max_age 
		- 单位 s 
		- 0 浏览器关闭失效
		- None 永不失效
	- expires 
		- datetime
		- timedelta
- 默认不支持中文，可以自行转换

- 获取cookie
```
request.COOKIES.get("name")
```
#### set_signed_cookie

- salt 加密，仍不支持中文 
- 获取需要解密
```
request.get_signed_cookie(content,salt='')#内容与加密时一样就行
```
#### 删除

```
response.delete_cookie(key)
```

### session

- 设置session

  ```
  request.session[key] = value
  ```

- 获取session

  ```
  request.session.get(key),没有返回None
  or
  request.seeion[key],没有报错
  ```

- 默认 混淆串+字符 进行Base64转码，所以支持中文

- 默认过期时间14天

- session依赖cookie 通过{sessionid：value} 以cookie形式保存

  ### token

  - 服务端会话技术

  - 自定义的session

  - web页面开发中，使用与session基本一致

  - 服务端与客户端，通常以json形式传输，需要移动端自己储存token，需要获取token关联数据的时候，主动传递token

### 对比

    - cookie 储存在本地，服务器压力小，数据不安全
    - session储存在服务器，需要维护，相对安全
    - token 是自定义session，自己维护相对麻烦，但支持更多终端
### csrf

- django中用于跨站请求伪造保护

- 防止恶意注册，确保客户端是自己的客户端

- 使用cookie中的csrftoken进行验证，传输

- 服务端发送给客户端，客户端将cookie获取过来，还要进行编码转换（数据安全)

- 跳过csrf

  - 添加标签

  ```
  {% csrf_token %}
  效果
  1.在请求头添加一个token
  2.页面加一个隐藏的input标签，内含token（从cookie获取）
  ```

  - 注释setting.py中middleware中csrf中间件
  - views方法中添加装饰器@csrf_exempt 豁免csrf验证

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


```

# 其他

## 编码

### hashlib

```
hashlib.new('编码',"数据").hexdigect()
返回bytes

```

## 缓存cache

- 缓存键
- 缓存值
  - 一般是base64+xx多种编码
  - 包含所有信息，请求头，content-type,页面内容等等
- 超时时间



### 缓存类型


- 使用数据库 django.core.cache.backends.db.DatabaseCache
- 使用本地内存 django.core.cache.backends.locmem.LocMemCache
- 使用文件系统 django.core.cache.backends.filebased.FileBasedCache
- 使用memcached django.core.cache.backends.memcached.MemcachedCache
- 使用redis
- 等
### 缓存功能

使用缓存后，views直接查询缓存，如果没有，再通过models获取数据，如果有直接
### django数据库缓存

- 创建缓存表

```
python manage.py createcachetable table_name
```

- 注册缓存

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'mycache_table',
        'TIMEOUT': '60',
        'OPTIONS': {
            'MAX_ENTRIES': '300',
        },
        'KEY_PREFIX': "dj",
        'VERSION': '1.0',
    }
```

- 使用缓存

```
from django.views.decorators.cache import cache_page
使用装饰器@cache_page即可
```

#### 注册参数

- BACKEND

  - 缓存类型

- LOCATION

  - 缓存到的位置
  - 不同缓存类型，location设置格式不同

- OPTIONS
  - MAX_ENTRIES 
    - 最大缓存条数
    - 默认300
  - CULL_FREQUENCY
    -  整数，
    - 当达到最大缓存数，淘汰的比例，1:CULL_FREQUENCY ,如CULL_FREQUENCY=2，淘汰一半
#### 使用参数
- timeout
  - 必要参数 单位秒
- cache
  - 字符串
  - 缓存库配置
  - 默认default
  - 多个缓存库时设置
- key_prefix



## 手动创建cache_page

### 获取缓存

- cache.get(key,deafult)

```python
#单个缓存
from django.core.cache import cache
#多个缓存
from django.core.cache import caches
local_cache = cache.get('unique_identifier')
if local_cache :
    return HttpResponse(local_cache)
```



### 手动缓存

```
res = render(request,'x.html'.content,context)
cache.set('unique_identifier',res.content,timeout=60)
return res
```

:smile:

## redis cache

1. 安装redis django支持包

   > pip install 	django-redis-cache

   > pip install django-redis

2. 数据库导入

   ```python
   'CACHE' : {'BACKEND':'django_redis.cache.RedisCache',
      'LOCATION':'redis://127.0.0.1:6379/1',#1是库名
      'OPTIONS':{
      'CLIENT_CLASS':'django_redis.client.DefaultClient'#单例,
       'PASSWORD':"123456"
      },
           }
       
   ```
## 可注册使用多个缓存

```python
CACHE = {
    'default':{},
    'redis':{}
}
```

### 手动缓存

```
cache = caches['cache_db_name']
result = cache.get()
cache.set()
```

## 分页器Paginator

- 自动对传入数据进行分页
- 参数
  - object_list
  - perpage int
  - f
  - allow_empty_first_page=True
- 方法
  - paginator.page(numberofpage)







# 中间件

- 轻量级，底层插件
- 可接入Django请求和相应过程
- 面向切面变成
- 本质是一个python类，装饰器

## 面向切面编程

- Aspect Oriented Programming AOP
- 实现针对业务处理过程中的切面进行提取
- 面对的是处理过程中的某个步骤或者阶段
- 以达到获取逻辑过程中各部分中间低耦合的隔离效果

## 作用

当使用中间后，相关作用自动生效，如process_request完成后，所有请求会自动通过process\_request,可以通过ip统计地区人数等，进行

- 数据分析
- 数据过滤
- 权重控制
- 黑白名单
- 优先级控制
- 反爬
- 频率控制

## 中间件功能

### process_request

- 客户端请求通过process_request,主动或默认返回
- 参数 self,request

### process_exception

- 捕获异常
- 默认None，返回None时，继续由下个中间件的process_exception处理
- 主动返回HttpResponse
- 顺序按照setting.py中中间件顺序执行
- 参数 self,request,exception

## 中间件使用

### 导入中间件

- 新建包middleware,创建middleware.py

- 中间件类继承MiddlewareMixin

```python
from django.utils.deprecation import MiddlewareMixin

class hellomiddle(MiddlewareMixin):
    
```

- settings.py注册新建的中间件

```python
MIDDLEWARE = [
    'middleware.middleware.hellomiddle'
]
```

### 中间件编写

#### 执行顺序

request - > process_request ->process_view->view->process_template_response-> request_response

process_exception全局

#### process_request

- 参数
  - self
  - request
- 顺序 获取请求后，views之前
- 中间件顺序 列表正序

```python
class hellomiddle(MiddlewareMixin):
    def process_request(self,request):
        ip = request.META.get('REMOTE_ADDR')
        #白名单
        if request.path =='/two/getphone':
			if request.META.get('REMOTE_ADDR') == '127.0.0.1':
    	    	return HttpResponse('抢单成功')
        #权重控制
        	if ip.startswith('10'):
                if random.randrange(100) >10:
                    return HttpResponse('中奖')
        #反爬
        if request.path = 'two/getdata':
            timeout = cache.get(ip)
            if timeout:
                return HttpResponse('10秒后再试')
            cache.set(ip,ip,timeout=10)
```

##### 单位时间内，数量控制器

```python
count = cache.get(ip)
            count = [] if count is None else count
            print(count)
            while count and time.time() - count[-1] > 60:
                count.pop()
                # 列表顺序为最新的时间index为0，所以最后一个元素距离现在超过60秒时，删除最后一个元素，遍历判断，直到每个元素距离现在都小于60秒
            if count:
                # 删除超过60秒的元素后，count数量仍大于3，说明60秒内访问次数超过3
                if len(count) >= 3:
                    return HttpResponse('60秒内访问过多，稍后再试')
            # 不论上面判断，每次访问都会增加一个当前时间，即使已经返回 访问过多
            count.insert(0, time.time())
            # 覆写缓存，把当前最新的访问时间次数列表写入缓存
            cache.set(ip, count, timeout=60)
```

#### process_view

- 视图函数前执行
- 参数 
  - self
  - request
  - view_func
  - view_args
  - view_kwargs
- 如果process_request返回HttpResponse，则不执行process_view

#### process_template_response

- 顺序

  > 视图函数执行后立刻执行

- 前提

  > 视图函数返回的对象有render方法（），或者返回的对象是TemplateResponse对象或等价方法

- 参数
  - self
  - request
  - response

#### preocess_response

- 执行完views.py后执行的函数
- 中间件顺序 中间件列表反序
- 参数
  - self
  - request
  - response
- 返回
  - HttpResponse对象（顶替views中的返回）

#### process_exception

- 捕获所有异常

- 参数

  - self
  - request
  - exception

- exception.__class__.__name__可以获取异常类型名字，进行详细处理

```python
    def process_exception(self, request, exception):
        res = redirect(reverse('two:hello'))
        return res
```



## 注意

- 缓存中数据无法修改，但是可以顶替
- cache.get(key,default)当返回未None时，返回默认数据

## 问题

1. 当process_request主动返回时，不同请求返回内容相同？

request.path进行判断

2. ‘/two/getphone’是是什么？url路径？

> 除了域名意外的请求路径,'/'开头
# coding=utf-8
import datetime
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import time


# Create your views here.

def user_login(request):  # 用户登录
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
        from django.contrib.auth import login, authenticate
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/blog/page123')
            else:
                return HttpResponse("用户尚未激活")
        else:
            return HttpResponse("用户名或密码错误")


def paginators(request):  # 分页
    from django.shortcuts import render
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    L = []
    for i in range(999):
        L.append(i + 1)
    page = request.GET.get('page')  # 当前页
    page_size = request.GET.get('pageSize')  # 每页数据数
    paginator = Paginator(L, page_size)
    # per_page: 每页显示条目数量
    # count: 数据总数
    # num_pages: 总页数
    # page_range： 总页数的索引范围，如:(1, 100)
    # page： page对象
    try:
        posts = paginator.page(page)
        # has_next 是否有下一页
        # next_page_number 下一页页码
        # has_previous 是否有上一页
        # previous_page_number 上一页页码
        # object_list 分页之后的数据列表
        # number 当前页
        # paginator paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'paginator.html', {'posts': posts})


def index(request):
    return render(request, 'home.html', {'title': '首页'})


def articles(request):
    return HttpResponse("This is articles page!")


def articles_year(request, year):
    return HttpResponse("The year is " + year + "!")


def articles_month(request, year, month):
    return HttpResponse("year " + year + ' ，month ' + month)


def news(request):
    return HttpResponse("This is news page!")


def news_year(request, year):
    return HttpResponse("This is news page! And this year is " + year)


def news_month(request, year, month):
    return HttpResponse("This is news page! And this year is " + year + ", the month is " + month)


def news_day(request, year, month, day):
    return HttpResponse("Year: " + year + " month: " + month + " day: " + day)


def news_id(request, id):
    return HttpResponse("The new Id is " + id)


def others(request):
    return HttpResponse("This is others pages!")


def others_history(request, history):
    return HttpResponse("This is other history page, and the history is " + history)


@login_required(login_url="/login")
def blog(request, num):
    """
    http请求中产生两个核心对象
        http请求：HttpRequest对象
        http响应：HttpResponse对象

    1.HttpRequest对象
        当请求一个页面时，Django创建一个HttpRequest对象包含原数据的请求，然后Django加载适当的视图，通过HttpRequest作为视图函数的第一个参数。每个视图负责返回一个HttpResponse目标

        path: 请求页面的全路径，不包括域名

        method: 请求中使用的HTTP方法的字符串表示，全大写表示，例如
            if request.method == 'GET':
                do_something()
            elseif request.method == 'POST':
                do_other()

        GET: 包含所有HTTP GET参数的类字典对象

        POST: 包含所有HTTP POST参数的类字典对象
            服务器收到空的POST请求的情况也是有可能发生的，表单form通过Http POST方法提交请求，但是表单中可能没有数据

        COOKIES: 包含所有cookies的标准python字典对象；keys和values都是字符串

        FILES: 包含所有上传文件的类字典对象；FILES中的每一个key都是<input type='file' name='' />标签中的name属性的值，FILES中的每一个value同时也是一个标准的python字典对象，包含了下面三个key:
            filename: 上传文件名，用字符串表示
            content_type: 上传文件的Content Type
            content: 上传文件的原始内容

        user: 一个django.auth.models.User对象，代表当前登录的用户。如果访问用户当前没有登录，user将被初始化为django.contrib.auth.models.AnonymousUser的实例。可以通过user的is_authenticated()方法来识别用户是否登录：
            if request.user.is_authenticated(); 只有激活Django中的AuthenticationMiddleware时该属性才可用

        session: 唯一可读写的属性，代表当前会话的字典对象；只有激活Django中的session时该属性才可用

        META: 一个标准的python字典包含所有可用的HTTP头，可用标题取决于客户端和服务器，但这里是一些例子：
            CONTENT_LENGTH          请求体的长度（一个字符串）
            CONTENT_TYPE            请求体的类型
            HTTP_ACCEPT             为响应可接受的内容类型
            HTTP_ACCEPT_ENCODING    接受编码的响应
            HTTP_ACCEPT_LANGUAGE    接受语言的响应
            HTTP_HOST               客户端发送的HTTP主机名
            HTTP_REFERER            参考页面
            HTTP_USER_AGENT         客户端的用户代理字符串
            QUERY_STRING            查询字符串，作为一个单一的（分析的）字符串
            REMOTE_HOST             客户端的主机名
            REMOTE_ADDR             客户端的IP地址
            REMOTE_USER             用户通过web服务器的身份验证
            REQUEST_METHOD          字符串，如“GET”或“POST”
            SERVER_NAME             服务器的主机名
            SERVER_PORT             服务器的端口（一个字符串）

    """

    """
    对于HttpRequest对象来说，是由Django自动创建的，但是HttpResponse对象就必须我们自己创建。每个view请求处理方法必须返回一个HttpResponse对象。在HttpResponse对象上扩展的常用方法如下：
        页面渲染：render(推荐)，render_to_response（对于页面的渲染方法中，render和render_to_response使用方法和功能类似，但render功能更强大，推荐使用）
        页面跳转：redirect
        locals: 可以直接将对应视图函数中的所有的变量传给模板
        
    """
    name = "robin.zhu"
    address = "xinXian"
    password = 'Any tags that are opened in the string and not closed before the truncation point are closed immediately after the truncation.'
    age = 88
    li = [1, 2, 3, 4, 5]
    str0 = ['a', 'b', 'c']
    # 获取当前时间戳
    now = time.time()
    # 转为为其他日期格式，如："%Y-%m-%d %H:%M:%S"
    time_locale = time.localtime(now)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S', time_locale)

    """
    render(request, template_name, context=None, content_type=None, status=None, using=None) 结合给定的模板与一个给定的上下文，返回一个字典HTTPResponse在渲染文本对象
        必选参数
            template_name  一个模板的使用或模板序列名称全称，如果序列是给定的，存在的第一个模板将被使用
        
        可选参数
            context 一组字典的值添加到模板中。默认情况下，这是一个空字典
            content_type MIME类型用于生成文档
            status 为响应状态代码。默认值为200
            using  用于加载模板使用的模板引擎的名称
    """

    """
    模板
        1.模板的执行
        模板的创建过程，对于模板其实就是读取模板（其中嵌套这模板标签），然后将Model中获取的数据插入到模板中，最后将信息返回给用户
    """

    """
    自定义标签
        因为在模板语言中不能做运算等一些稍显复杂的操作，所以在Django中提供了两种自定制标签，一种是simple_tag，一种是filter
        simple_tag：任意传递参数，但不能用布尔判断
        filter: 最多只能传递两个参数，可用作布尔判断
    """
    from .models import user_info, Host, UserGroup
    # user_info.objects.create(name=u"jack", email=u"1037571865@qq.com", memo=u"jack的个人简介") # 增
    # users = user_info.objects.all()
    # print(users)

    """
    进阶操作(了不起的双下划綫)
        数量 user_info.objects.filter().count()
        
        大于、小于
            user_info.objects.filter(id__gt=3) id大于3
            user_info.objects.filter(id__gte=3) id大于或等于3
            user_info.objects.filter(id__lt=2) id小于2
            user_info.objects.filter(id__lte=2) id小于或等于2
            user_info.objects.filter(id__gt=2, id__lt=5) id大于2小于5
            
        in
            user_info.objects.filter(id__in=[1, 2, 3])  id等于1、2、3的用户
            user_info.objects.exclude(id__in=[1, 2, 3]) id不在1、2、3之中的用户
            
        isnull
            user_info.objects.filter(add_time__isnull=True)    
            
        contains
            user_info.objects.filter(name__contains=u"朱") name中包含"朱"的用户
            user_info.objects.filter(name__icontains=u'J') name中包含'J'的用户 （icontains大小写不敏感）
            
        range
            user_info.objects.filter(id__range=[3, 5]) id在3到5之间的用户
            
        其他类似
            startswith, istartswith, endswith, iendswith       
            
        order by（排序）
            user_info.objects.filter().order_by('id') # asc 正序
            user_info.objects.filter().order_by('_id') # desc 倒序    
            
        limit、offset
            user_info.objects.all()[10:20] 取11-20的数据     
            
        regex正则匹配，iregex不区分大小写
            user_info.objects.get(name__regex=r'^j+')
            user_info.objects.get(name__iregex=r'^j+')
            
        date 日期
            user_info.objects.filter(add_time__date=datetime.date(2018, 1, 10))
            user_info.objects.filter(add_time__date__lt=datetime.date(2019, 1, 1)) 添加时间早于2019年1月1日
            
        year 年份
            user_info.objects.filter(add_time__year=2018) 添加年份为2018的 
            
        month 月份
            user_info.objects.filter(add_time__month=8) 添加月份为8的    
            
        day 日
            user_info.objects.filter(add_time__day=8) 添加日为8的
            
        week_day 星期
            user_info.objects.filter(add_time__week_day=1) 添加时间为星期日的
            week_day取值如下：
                Sunday: 1
                Monday: 2
                Tuesday: 3
                Wednesday: 4
                Friday: 6
                Saturday: 7     
                
        hour minute second 时分秒
            与day类似        
            
    """
    count = user_info.objects.filter().count()
    user1 = user_info.objects.filter(id__gte=3)
    user2 = user_info.objects.filter(id__gt=3)
    user3 = user_info.objects.filter(id__lt=2)
    user4 = user_info.objects.filter(id__lte=2)
    user5 = user_info.objects.filter(id__gt=2, id__lt=5)
    user6 = user_info.objects.filter(id__in=[1, 2, 3])
    user7 = user_info.objects.exclude(id__in=[1, 2, 3])
    user8 = user_info.objects.filter(name__contains=u'朱')
    user9 = user_info.objects.filter(name__icontains='J')
    user10 = user_info.objects.filter(name__iendswith=u'康')
    user11 = user_info.objects.filter().order_by('id')
    user12 = user_info.objects.filter().order_by('-id')
    user13 = user_info.objects.filter()[6:10]
    user14 = user_info.objects.filter(name__regex=r'^j+')
    user15 = user_info.objects.filter(name__iregex=r'^j+')
    user16 = user_info.objects.filter(add_time__date__lt=datetime.date(2018, 4, 11))
    user17 = user_info.objects.filter(add_time__year=2018)
    user18 = user_info.objects.filter(add_time__month=8)
    user19 = user_info.objects.filter(add_time__day=12)
    user20 = user_info.objects.filter(add_time__week_day=7)

    print('%s:%s' % ('用户数量', count))
    print('{0}{1}'.format('id大于或等于3的用户', user1))
    print('{0}{1}'.format('id大于3的用户', user2))
    print('{0}{1}'.format('id小于2的用户', user3))
    print('{0}{1}'.format('id小于或等于2的用户', user4))
    print('{0}{1}'.format('id大于2小于5的用户', user5))
    print('{0}{1}'.format('id等于1、2、3的用户', user6))
    print('{0}{1}'.format('id不在1、2、3之中的用户', user7))
    print('{0}{1}'.format('name包含‘朱’的用户', user8))
    print('{0}{1}'.format('name包含J的用户', user9))
    print('{0}{1}'.format('name以康结尾的用户', user10))
    print(user14, user15, user16)

    # 添加一对多
    # dic = {
    #     'hostname': '123321',
    #     'ip': '192.168.1.1',
    #     'user_group_id': 2
    # }
    # Host.objects.create(**dic)
    # # 正向查询一对多
    # host_obj = Host.objects.all()
    # print(host_obj)

    print(Host.objects.filter(user_group__caption="标题1"))

    # 反向查询一对多
    # usergroup_obj = UserGroup.objects.get(id=1)
    # print(usergroup_obj.caption)
    # print(usergroup_obj.host_set.all())  # 所有关于id=1的host
    #
    # # 增删改查
    # group_obj = UserGroup.objects.get(caption='集群管理员')
    # print(group_obj)
    # group_objs = UserGroup.objects.all()
    # print(group_objs[1].user_info)

    # 新建用户
    # add_user()

    # 认证用户
    # auth_user()

    # 修改密码
    # change_password()

    # 登录
    # login(request)

    # 登出
    # logout(request)
    return render(request, "blog.html", locals(), content_type="")


def my_serializers(request):
    from django.core import serializers
    from .models import user_info
    ret = user_info.objects.all()
    data = serializers.serialize('json', ret)
    return HttpResponse(data)


def add_user():  # 新建用户
    from django.contrib.auth.models import User
    user = User.objects.create_user("robin.zhu", '1037571865@qq.com', 'zdp19850829')
    user.save()  # 不存储用户密码明文而是存储一个Hash值


def auth_user():  # 认证用户
    from django.contrib.auth import authenticate
    user = authenticate(username='robin.zhu', password='zdp198508290')
    # 认证用户的密码是否有效，若有效则返回代表该用户的user对象，若无效则返回None。该方法不检查is_active标志位
    print(user)


def change_password():  # 修改密码
    # 以下实例为先认证通过后才可以修改密码
    from django.contrib.auth import authenticate
    user = authenticate(username='robin.zhu', password='zdp19850829')
    if user is not None:
        user.set_password('zdp198508290')
        user.save()


def login(request):  # 登录
    from django.contrib.auth import authenticate
    from django.contrib.auth import login
    # login向session中添加session_key，便于对用户进行跟踪
    # login不进行认证，也不检查is_active标志位
    user = authenticate(username='robin.zhu', password='zdp198508290')
    if user is not None:
        if user.is_active:
            login(request, user)


def logout(request):
    # logout会移除request中user信息，并刷新session
    from django.contrib.auth import logout
    logout(request)

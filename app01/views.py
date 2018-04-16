from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils.timezone import now
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

# def index(request):
#     contxet ={}   #字典
#     # 获取模板对象
#     template = loader.get_template('index.html')
#     # 渲染模板对象
#     html_str = contxet = template.render(contxet, request)
#     return HttpResponse(html_str)
# # from django.template.defaulttags import now


class Student(object):
    # name = 'Tom'
    def name(self):
        return 'name'


def index(request):
    my_dict = {'key01': 'value01', 'key02': 'value01'}
    my_list = ['列表01', '列表02', '列表03', '列表04']
    my_obj = Student()
    my_date = now()

    context = {
        'number': 5,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_obj': my_obj,
        'my_date': my_date,
          }
    return render(request, 'index.html', context)


def index1(request):
    my_html = '<font color="red">红色</font>'
    context = {
        'my_html': my_html
          }
    return render(request, 'index.html', context)


def inherit(request):

    return render(request, 'child.html')


def show_news(request, a, b):
    return HttpResponse("新闻界面：%s %s" % (a, b))


def show_news2(request, category, page_no):
    return HttpResponse("新闻界面2：%s %s" % (category, page_no))


def create_verify_code(request):
    """使用Pillow包生成验证码图片"""

    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100), 255)  # RGB

    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)

    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'

    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)

    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def show_verify_codele(request):
    return render(request, 'show__verify_code.html')


def do_verify_codele(request):
    # 获取客户填写的验证码
    code = request.POST.get('verify_code')

    # 获取图片session填写的验证码
    code1 = request.session.get('verifycode')
    if code.upper()== code1.upper():
        return HttpResponse('验证通过')
    else:
        return HttpResponse('验证不通过')


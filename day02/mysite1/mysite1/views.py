from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# day 1

def index_view(request):

    html = '<h1>Home</h1>'
    return HttpResponse(html)


def page_1_view(request):

    html = '<h1>Page 1</h1>'
    return HttpResponse(html)


def page_2_view(request):

    html = '<h1>Page 2</h1>'
    return HttpResponse(html)


def pagen_view(request, pg):

    html = f'<h1>Page {pg}</h1>'
    return HttpResponse(html)


def page_2003_view(request):

    html = '<h1>Page 2003</h1>'
    return HttpResponse(html)


def cal2_view(request, v1, op, v2):
    html = 'Only 2: '
    calc = {
        'add': ['+', lambda x, y: int(x) + int(y)],
        'sub': ['-', lambda x, y: int(x) - int(y)],
        'mul': ['*', lambda x, y: int(x) * int(y)],
    }

    if op in calc.keys():
        html += f'{int(v1)} {calc[op][0]} {v2} = {calc[op][1](v1, v2)}'
        return HttpResponse(html)

    html = f'Invalid expression'
    return HttpResponse(html)


def cal_view(request, v1, op, v2):
    html = 'All: '
    calc = {
        'add': ['+', lambda x, y: x + y],
        'sub': ['-', lambda x, y: x - y],
        'mul': ['*', lambda x, y: x * y],
    }

    if op in calc.keys():
        html += f'{int(v1)} {calc[op][0]} {v2} = {calc[op][1](v1, v2)}'
        return HttpResponse(html)

    html = f'Invalid expression'
    return HttpResponse(html)


def birthday_view(request, year, month, day):
    html = f'{year}-{month}-{day}'
    return HttpResponse(html)


# day 2

POST_FORM = '''
<form method="POST" action='/test_get_post'>
    USERNAME <input type="text" name="uname">: 
    <input type="submit" value="valid">
</form>
'''


def test_request(request):
    print('path info is', request.path_info)
    print('method is', request.method)
    print('querystring is', request.GET)
    print('full path', request.get_full_path())

    return HttpResponse('test request ok')


def test_get_post(request):
    if request.method == 'GET':
        # print(request.GET['a'])
        # multi value with same key
        print(request.GET.getlist('a'))
        print(request.GET.get('c', 'no c'))

        return HttpResponse(POST_FORM)

    elif request.method == 'POST':
        print('post, get:', request.GET)
        print('post, post', request.POST)
        print('uname is', request.POST['uname'])
        return HttpResponse('test post ok')
    else:
        pass

    return HttpResponse('test get post ok')


def test_html(request):
    # method 1: from django.template import loader

    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)

    # method 2: from django.shortcuts import render

    dic = {
        'username': 'dic test',
        'age': 18,
    }
    return render(request, 'test_html.html', dic)


def test_html_param(request):

    def say_hi():
        return 'hi'

    class Dog:
        def say(self):
            return 'woof'

    dic = {}
    dic['int'] = 88
    dic['str'] = 'str test'
    dic['lst'] = [1, 2, 3, 4, 5]
    dic['dict'] = {'a': 1, 'b': 2, 'c': 3}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    # dic['script'] = '<script>alert(111)</script>'

    return render(request, 'test_html_param.html', dic)


def test_if_for(request):

    dic = {}
    dic['x'] = 10
    dic['lst'] = ['tom', 'jack', 'lily']
    return render(request, 'test_if_for.html', dic)


def test_mycal(request):
    cal_op = {
        'add': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'div': lambda x, y: x / y,
    }

    def get():
        x = 0
        y = 0
        result = 0

        # use locals() to get all variables in current scope transform to dict
        return render(request, 'test_mycal.html', locals())

    def post():
        dic = {}
        dic['x'] = request.POST.get('x', 0)
        dic['y'] = request.POST.get('y', 0)
        dic['op'] = request.POST.get('op', 'add')
        dic['result'] = 0

        if dic['op'] in cal_op.keys():
            dic['result'] = cal_op[dic['op']](int(dic['x']), int(dic['y']))

        return render(request, 'test_mycal.html', dic)

    mth = {
        'GET': get,
        'POST': post,
    }

    return mth[request.method]()


def base_view(request):
    lst = ['Tom', 'Jack']
    return render(request, 'base.html', locals())


def music_view(request):

    return render(request, 'music.html')


def sport_view(request):

    return render(request, 'sport.html')


def test_url(request):

    return render(request, 'test_url.html')


def test_url_result(request, age):

    # 302 redirect
    from django.urls import reverse

    url = reverse('base_index')
    return HttpResponseRedirect(url)

    # return HttpResponse('test url result ok')
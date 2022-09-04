from django.http import HttpResponse


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

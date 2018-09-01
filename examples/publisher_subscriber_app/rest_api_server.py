import time

from algebra import area_circle
from bottle import *


@route('/')
def welcome():
    response.set_header('Vary', 'Accept')
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1>Hello!</h1>'

    response.content_type = 'text/plain'
    return 'Hello'


@route('/now')
def time_service():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age=1')
    return time.ctime()


@route('/upper/<word>')
def upper_case_service(word):
    response.content_type = 'text/plain'
    return word.upper()


@route('/area/circle')
def circle_area_service():
    response.set_header('Vary', 'Accept')
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
        return e.args[0]

    area = area_circle(radius)

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return f'<p> The area is <em> {area} </em> </p>'

    response.content_type = 'application/json'
    return dict(radius=radius, area=area, service=request.path)


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)

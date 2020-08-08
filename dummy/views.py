from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import datetime

# Create your views here.

def current_datetime(request):

    # response = HttpResponse()
    # response.content = "Hello World"
    # return response
    # or can be written as
    # return HttpResponse("Hello World")

    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" %now
    return HttpResponse(html)

def profile(request, username):
    # logics

    data = {
        'ram': 'Ram Bahadur',
        'hari': 'Hari Bahadur',
        'shyam': 'Shyam Bahadur',

    }

    # full_name = data[username]
    full_name = data.get(username) # return None if not found

    if not full_name:
        # return HttpResponseNotFound("The username does not exits")
        return HttpResponse("The username does not exists", status=404)

    string_data = f"Your full name is: {full_name}"

    return HttpResponse(string_data)

def profile_json(request, username):
    data = {
        'ram': 'Ram Bahadur',
        'hari': 'Hari Bahadur',
        'shyam': 'Shyam Bahadur',
    }
    full_name = data.get(username)

    if not full_name:
        return HttpResponse("The username does not exists", status=404)

    dict_data = {
        'full_name': full_name
    }

    return JsonResponse(dict_data)

def int_converter_path_view(request, int_data):
    print('int data is', int_data)
    print(type(int_data))
    try:
        _ = int(int_data)
    except ValueError:
        return HttpResponse("Something is wrong", status=404)

    return HttpResponse("OK Ok OK")

def debug_request(request):

    print("Request method:", request.method)
    print("Scheme:", request.scheme)
    print("Headers:", request.headers)
    print("REQUEST GET:", request.GET)

    return HttpResponse("Ok from debug")

def test_args_kwargs(request, *args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

    data = kwargs['data']

    string_data = "OK " * data

    return HttpResponse(string_data)

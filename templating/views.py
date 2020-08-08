from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def hello_templates(request):
    template = loader.get_template('hello.html')
    context = {
        'name': 'Ram Bahadur'
    }
    template_data = template.render(context, request)
    return HttpResponse(template_data)

def hello_render(request):
    context = {
        'name': 'Ram Bahadur',
        'my_dict': {
            'name': 'My name is Ram Bahadur'
        },

    }
    return render(request, "hello_render.html", context)






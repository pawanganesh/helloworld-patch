from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import FileModel

def render_static(request):
    return render(request, 'static.html')


def manage_media(request):

    if request.method == 'POST':
        print("Post Data: ", request.POST)
        print("Files: ", request.FILES)
        if 'name' in request.POST and 'myfile' in request.FILES:
            file_obj = request.FILES['myfile']
            full_name = request.POST['name']

            obj = FileModel()
            obj.name = full_name
            obj.file = file_obj
            obj.save()

            return HttpResponse("Everything is okay")

            # print("My file name is", file_obj.name)
            # fs = FileSystemStorage()
            #
            # reference = fs.save(file_obj.name, file_obj)
            #
            # file_url = fs.url(reference)
            #
            # obj = FileModel()
            # obj.name = full_name
            # obj.file = reference
            # obj.save()
            #
            # print("After Save Filename is", reference)
            # print('My file URL is', file_url)
        else:
            return HttpResponse('Invalid')

    return render(request, 'media.html')






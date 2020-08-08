from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserInfoModelForm

from .models import UserInfo

# Create your views here.
def list_all_user(request):
    data = UserInfo.objects.all()
    context = {
        'data': data
    }
    return render(request, 'crud/list.html', context=context)

def detail_view_of_users(request, user_id):
    user_obj = get_object_or_404(UserInfo, id=user_id)
    # user_obj = UserInfo.objects.get(id=user_id)
    return render(request, 'crud/detail.html', context={
        'user_obj': user_obj
    })

def create_user_info(request):
    if request.method == "POST":
        form = UserInfoModelform(request.POST)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return  redirect('/crud/list/')
        else:
            print("Form is invalid")

    else:
        form = UserInfoModelform()

    return render(request, 'crud/create.html', context={
        'form': form
    })

def update_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    if request.method == "POST":
        form = UserInfoModelForm(request.POST, instance=user_object)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return  redirect(f'/crud/detail/{user_id}')
        else:
            print("Form is invalid")

    else:
        form = UserInfoModelform(instance=user_object)

    return render(request, 'crud/update.html', context={
        'form': form
    })

def delete_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo ,id=user_id)

    user_object.delete()
    return redirect(f'/crud/list/')














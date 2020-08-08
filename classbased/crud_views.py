from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .froms import UserInfoModelForm

from .models import UserInfo


class Create(CreateView):
    form_class = UserInfoModelForm
    template_name = 'classbased/create.html'
    # success_url = '/c/list' # classbase:list
    success_url = reverse_lazy('classbased:list')

    # def get_success_url(self):
    #     return reverse()

class List(ListView):
    template_name = 'classbased/list.html'
    model = UserInfo
    # model = UserInfo
    # or
    # queryset = UserInfo.objects.all()
    context_object_name = 'data'

    # def get_context_object_name(self, object_list):
        # send extra data
        # context = super(List, self).get_context_object_name()
        # pass

    # For logical processing
    # or
    # def get_queryset(self):
    #     if self.request.user == 1:
    #         return UserInfo.objects.all()
    #     else:
    #         return UserInfo.objects.filter(is_active=True)

class Detail(DetailView):
    model = UserInfo
    template_name = 'classbased/detail.html'
    # pk_url_kwarg = 'id'
    context_object_name = 'user_obj' # either we can
    # directly use 'object' in template

class Update(UpdateView):
    form_class = UserInfoModelForm
    pk_url_kwarg = 'id'
    success_url = '/c/list'
    model = UserInfo
    template_name = 'classbased/update.html'

    def form_valid(self, form):
        print("Form is valid")
        # my logic
        return super().form_valid(form)

    def form_invalid(self, form):
        pass

class Delete(DeleteView):
    # pk_url_kwarg = 'id'
    model = UserInfo
    success_url = '/c/list/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)




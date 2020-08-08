from django.urls import path
from .views import StatusMessageCreateView, StatusMessageDeleteView

app_name = 'statusapp'
urlpatterns = [
    path('create/', StatusMessageCreateView.as_view(), name="create"),
    path('delete/<int:id>/', StatusMessageDeleteView.as_view(), name="delete"),
]
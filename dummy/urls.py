from django.urls import path, register_converter
from . import views


# regex, to_python(), to_url()

class YearPathConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        int_data = int(value)

        if int_data > 2020:
            raise ValueError
        return int_data

    def to_url(self, value):
        return str(value)

register_converter(YearPathConverter, 'yyyy')

urlpatterns = [
    path('', views.current_datetime, name="current_time"),
    path('profile/<str:username>/', views.profile),
    path('profile-json/<str:username>/', views.profile_json),
    path('path/<str:int_data>/', views.int_converter_path_view),
    path('test-path/', views.debug_request),

    # custom path converter
    path('example/<yyyy:int_data>/', views.int_converter_path_view),
    path('test/<int:data>/', views.test_args_kwargs),




]

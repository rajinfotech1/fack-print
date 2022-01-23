from django.urls import path, re_path
from printAdhar import views

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    # re_path(r'^adhar_form_first/$', views.adhar_form_first, name="adhar_form_first"),
    re_path(r'^adhar_form/$', views.adhar_form, name="adhar_form"),
    re_path(r'^adhar_list/$', views.adhar_list, name="adhar_list"),
    re_path(r'^view_adhar/(?P<id>\d+)/$', views.view_adhar, name="view_adhar"),
    re_path(r'^update_adhar/(?P<id>\d+)/$', views.update_adhar, name="update_adhar"),
    re_path(r'^delete_adhar/(?P<id>\d+)/$', views.delete_adhar, name="delete_adhar"),
]

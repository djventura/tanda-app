from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('user', views.get_user, name="user"),
    path('role', views.role_list, name="role"),
    path('rule', views.rule_list, name="rule"),
    # path('person', views.getPerson, name="person"),
    # path('musician', views.getMusician, name="musician"),

]

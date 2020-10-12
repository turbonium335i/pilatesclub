from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('addmember', views.newmember, name='add_member'),
    path('operations', views.operations, name='operations'),
    path('lessons', views.lessons, name='lessons'),
    path('search', views.searchfilter, name='search'),
    path('vocab', views.vocab, name='vocab'),
    path('memberinfo/<str:pk>', views.memberinfo, name='memberinfo'),
    path('generateword/<str:pk>', views.generateWord, name='generateword'),
    path('wordput', views.wordput, name='wordput'),
    path('api/', views.apiOverview, name='apioverview'),
    path('apimembers/', views.memberList, name='apimemberlist'),
    path('javacore/', views.javacore, name='javacore'),


]
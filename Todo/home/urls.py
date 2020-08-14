from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('del/<int:del_key>/', views.del_task),			
]
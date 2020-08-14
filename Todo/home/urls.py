from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('del/<int:del_key>/', views.del_task),
	path('done/<int:task_key>/', views.task_done),			
]
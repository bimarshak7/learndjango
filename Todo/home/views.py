from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task


def home(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			new_task= request.POST["new_task"]
			task=Task()
			task.title=new_task
			task.user_id=request.user.id
			task.save()
			messages.info(request,"Task Added Sucessfully")
			return redirect('/home')
		else:
			tasks= Task.objects.filter(user_id=request.user.id)
			context= {'tasks': tasks}

			return render(request,'home.html',context)
	else:
		messages.info(request,"Please Sign In first")
		return redirect('/')

def del_task(request,del_key):
	Task.objects.get(id=del_key).delete()
	messages.info(request,'Task Deleted')
	return redirect('/home')

def task_done(request,task_key):
	task=Task.objects.get(id=task_key)
	task.done=True
	task.save()
	return redirect('/home')


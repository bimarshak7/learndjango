from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
	if request.method=='POST':
		username= request.POST["user_name"]
		password= request.POST["password"]

		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/home')
		else:
			messages.info(request,"Incorrect Username or Password")


	return render(request,'login.html')

def register(request):
	if request.method=='POST':
		first_name= request.POST["first_name"]
		last_name= request.POST["last_name"]
		email= request.POST["email"]
		username= request.POST["user_name"]
		password= request.POST["password"]
		confirm_password= request.POST["confirm_password"]

		if password==confirm_password:
			if User.objects.filter(username=username).exists():
				messages.info(request,"User already taken")
			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email Already Used")
			else:

				user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
				user.save()
				messages.info(request,"Account Created Sucessfully")
				return redirect('/')
		else:
			messages.info(request,"Passwords did not match")
	return render(request,'register.html')


def logout(request):
	auth.logout(request)
	return redirect('/')
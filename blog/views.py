from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from blog.models import newuserentry
from django.http import HttpResponse
from blog.models import blogpost
from datetime import datetime
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
dt,at={},{}
lt=[]
un,k='',""
u=''
a=''
posts=[{'title':'Welcome to my awesome blog app'
,'author':'Arpit Agarwal',
'content':'This is a blog app which was made by me.I used django framework of python to developed it.Share your views for this app.Hope you like it.',
'date_posted':'22 March,2019'}]
def signup(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			'''n=request.POST.get("username")
			e=request.POST.get("email")
			ph=request.POST.get("phone")
			p=request.POST.get("password1")
			p2=request.POST.get("password2")
			nwet=newuserentry(name=n,email=e,phone=ph,password=p)
			nwet.save()
			return render(request,'blog/redirectlogin.html',{})'''
			form.save()
			messages.success(request,'Account created succesfully')
			return render(request,'blog/redirectlogin.html',{})
			
			
	else:
		form=UserCreationForm()
	return render(request,'blog/signuptest.html',{'form':form})
def home(request):
	context={'posts':posts}
	return render(request,'blog/home.html',context)
def about(request):
	return render(request,'blog/about.html',{'title':'about'})
def login(request):
	return render(request,'blog/login.html',{})	
def registration(request):
	form=UserCreationForm()
	return render(request,'blog/signuptest.html',{'form':form})	
@csrf_exempt	
def newusersavedata(request):
	if request.method=="POST":
		n=request.POST.get("username")
		e=request.POST.get("email")
		ph=request.POST.get("phone")
		p=request.POST.get("password")
		nwet=newuserentry(name=n,email=e,phone=ph,password=p)
		nwet.save()
		return render(request,'blog/redirectlogin.html',{})
@csrf_exempt
def checkuserdata(request):
	if request.method=="POST":
		form=AuthenticationForm(data=request.POST)
		u=request.POST.get('username')
		p=request.POST.get('password')
		objects=newuserentry.objects.all()
		lt=[{'uname':u,'upass':p}]
	
		at=dt.copy()
		
		context={
		'lt':lt
		}
		if form.is_valid():
			return render(request,'blog/postform.html',context)
		else:
			form=AuthenticationForm()
			return HttpResponse("<h1>No such data</h1>")		

		'''u=request.POST.get('username')
		p=request.POST.get('password')
		objects=newuserentry.objects.all()
		lt=[{'uname':u,'upass':p}]
	
		at=dt.copy()
		
		context={
		'lt':lt
		}
		
		for x in objects:
			if(u==x.name and p==x.password):
				name_1=u
				return render(request,'blog/postform.html',context)
				
				return 

		else:
			return HttpResponse("<h1>No such data</h1>")'''		
				
@csrf_exempt	
def saveblogpost(request):
	if request.method=="POST":
		a=request.POST.get("author")
		k=a
		t=request.POST.get("title")
		c=request.POST.get("content")
		d=datetime.now()
		formatedDate = d.strftime("%Y-%m-%d %H:%M:%S")
		if(a=='' or t=='' or c=='' or d==''):
			return HttpResponse("<h1>Please create the valid post")
		else:
			bp=blogpost(author=a,title=t,content=c,date_posted=formatedDate)
			bp.save()
			obj=blogpost.objects.filter(author=a)
			if obj.exists():
				res=""
				mypost=[]
				for x in obj:
					au=res+x.author
					ti=res+x.title
					co=res+x.content
					da=res+str(x.date_posted)
					myp={'title':ti,'author':au,'content':co,'date_posted':da}
					for i in range(0,1):
						mypost.insert(i,myp)	
				contexttwo={'mypost':mypost}
				return render(request,'blog/showblogpage.html',contexttwo)
			else:
				return HttpResponse("<H1>You have zero post to show....</H1>")
			'''return render(request,'blog/showuserpost.html',{})'''
@csrf_exempt
def showmypost(request):
	if request.method=="POST":
		k=request.POST.get("authorone")
	obj=blogpost.objects.filter(author=k)
	if obj.exists():
		res=""
		mypost=[]
		for x in obj:
			au=res+x.author
			ti=res+x.title
			co=res+x.content
			da=res+str(x.date_posted)
			myp={'title':ti,'author':au,'content':co,'date_posted':da}
			for i in range(0,1):
				mypost.insert(i,myp)	
		contexttwo={'mypost':mypost}
		return render(request,'blog/showblogpage.html',contexttwo)
	else:
		return HttpResponse("<H1>You have zero post to show....</H1>")	
@csrf_exempt
def showotherpost(request):
	if request.method=='POST':
		amy=request.POST.get('authorfive')
		obj=blogpost.objects.all()
	res=""
	mypost=[]
	for x in obj:
		au=res+x.author
		ti=res+x.title
		co=res+x.content
		da=res+str(x.date_posted)
		myp={'title':ti,'author':au,'content':co,'date_posted':da,'uname':amy}
		for i in range(0,1):
			mypost.insert(i,myp)	
	contextthree={'mypost':mypost}
	return render(request,'blog/mybasetwo.html',contextthree)	
@csrf_exempt
def newpost(request):
	if request.method=="POST":
		aut=request.POST.get("authorfour")
	lt=[{'uname':aut}]
	contextfour={
	'lt':lt
	}	
	return render(request,'blog/postform.html',contextfour)
def forgotpassword(request):
	'''ltp=['arpitagarwal916.aa@gmail.com']
	res=send_mail("Hello arpit","hi it work",'arpitagarwal990@gmail.com',ltp,fail_silently=True)
	'''
	return HttpResponse("<h1>This feature will be added soon...")	
def logout(request):
	return render(request,"blog/logout.html",{})	
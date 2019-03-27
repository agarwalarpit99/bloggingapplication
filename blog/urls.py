from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('home/',views.home,name='home'),
    path('login/',views.login),
    path('about/',views.about,name="blog-about"),
    path('registration/',views.registration,name="blog-regis"),
    path('newusersavedata/',views.newusersavedata,name="blog-newuserentry"),
	path('checkuserdata/',views.checkuserdata),
	path('saveblogpost/',views.saveblogpost),
	path('showmypost/',views.showmypost),
	path('showotherpost/',views.showotherpost),
	path('newpost/',views.newpost),
	path('signup/',views.signup),
	path('forgotpassword/',views.forgotpassword),
	path('logout/',views.logout),
	]

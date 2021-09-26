from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request ,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	#return HttpResponse("<h1> Hello World</h1>")
	return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
	return render(request,"contact.html",{})
def about_view(request ,*args,**kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_email": "amirzand2002@gmail.com",
		"my_list": ["bachelorat of HUT","graduate from BASU"]
	}
	return render(request,"about.html",my_context)
def social_view(*args,**kwargs):
	return HttpResponse("<h1> Social page</h1>")


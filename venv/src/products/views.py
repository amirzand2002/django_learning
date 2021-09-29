from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product
from .forms import ProductForm
# Create your views here.


def product_create_view(request):
 	form = ProductForm(request.POST or None)
 	if form.is_valid():
 		form.save()
 		form = ProductForm()
 	context = {
 		'form':form
 	}
 	return render(request, "products/product_create.html",context)
## 3:03:17 inja error mide 
def product_update_view(request,id=id):
    obj = get_object_or_404(Product,id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
 		#form = ProductForm()
    context = {
        'form':form
    }
    return render(request, "products/product_create.html",context)


def product_detail_view(request,id=id):
	obj = get_object_or_404(Product, id=id)
	#context = {
	#	'title':obj.title,
	#	'description':obj.description,
	#	'price':obj.price
	#}
	context = {
		'object':obj
	}
	return render(request, "products/product_detail.html",context)


def dynamic_lookup_view(request,id):
	#obj = Product.objects.get(id=id)
	obj = get_object_or_404(Product, id = id )
	# try:
	# 	obj = Product.objects.get(id=id)
	# except Product.DoesNotExist:
	# 	raise Http404
	context={
	 	"object":obj
	}
	return render(request,"products/product_detail.html",context)


def product_delete_view(request,id):
	obj = get_object_or_404(Product, id=id)

	if request.method=="POST":
		obj.delete()
		return redirect('../../../')
	context={

		"object":obj	
		}
	return render(request,"products/product_delete.html",context)


def product_list_view(request):
	queryset = Product.objects.all()
	context ={
		"object_list":queryset
	}
	return render(request,"products/product_list.html",context)
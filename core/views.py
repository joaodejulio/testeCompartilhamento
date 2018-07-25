from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#texts = ['batata123', 'vamo ve oq rola']

	#context = {
	#	'title':'éoq? ',
	#	'texts': texts

	#}
	#testando
	return render(request, 'index.html') #quando usar a parte comentada colocar isso dps do index.html: , context


def contact(request):
	return render(request, 'contact.html')

def products(request):
	return render(request, 'products.html')

def product_list(request):
	return render(request, 'product_list.html')			

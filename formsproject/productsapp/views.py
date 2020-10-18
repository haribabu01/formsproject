from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from productsapp.forms import ProductForm
from productsapp.models import ProductModel

import json
# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class InsertOneProduct(View):
	def post(self,request):
		# print(request.body) # it will return binary string
		data = request.body
		json_data = json.loads(data)
		pf = ProductForm(json_data)
		if pf.is_valid():
			pf.save()
			response = json.dumps({"success":"Product is saved"})
		else:
			response = json.dumps(pf.errors)
		return HttpResponse(response, content_type="application/json")

@method_decorator(csrf_exempt,name="dispatch")
class UpdateOneProduct(View):
	def put(self,request,product):
		try:
			old_product = ProductModel.objects.get(no=product)
			new_product = json.loads(request.body)
			pf = ProductForm(new_product,instance=old_product)
			if pf.is_valid():
				pf.save()
				json_data = json.dumps({"success": "Product is updated"})
			else:
				json_data = json.dumps(pf.errors)
			return HttpResponse(json_data, content_type="application/json")
		except ProductModel.DoesNotExist:
			json_data = json.dumps({"error": "Invalid Product No"})
			return HttpResponse(json_data, content_type="application/json")

@method_decorator(csrf_exempt,name="dispatch")
class UpdateOneProduct2(View):
	def put(self,request,product):
		try:
			old_product = ProductModel.objects.get(no=product)

			new_product = json.loads(request.body)
			
			"""
			new data
			{
			    "no": 5001,
				"name": "iphone6s", 
				"price": 12000
				"quantity": 200
			}
			
			old_data
			{
			    "no": 5001,
				"name": "iphone6s", 
				"price": 2000
				"quantity": 20
			}
			"""
			data = {
				"no": old_product.no,
				"name": old_product.name,
				"price": old_product.price,
				"quantity": old_product.quantity
			}

			for key,value in new_product.items():
				data[key] = value
			pf = ProductForm(data,instance=old_product)
			if pf.is_valid():
				pf.save()
				json_data = json.dumps({"success": "Product is updated"})
			else:
				json_data = json.dumps(pf.errors)
			return HttpResponse(json_data, content_type="application/json")
		except ProductModel.DoesNotExist:
			json_data = json.dumps({"error": "Invalid Product No"})
			return HttpResponse(json_data, content_type="application/json")



@method_decorator(csrf_exempt,name="dispatch")
class DeleteOneProduct(View):
	def delete(self,request,product):
		try:
			res = ProductModel.objects.get(no=product).delete()
			print(res)
			if res[0] == 1:
				json_data = json.dumps({"message": "Product is Deleted"})
				return HttpResponse(json_data, content_type="application/json")
		except ProductModel.DoesNotExist:
			json_data = json.dumps({"error": "Invalid Product No"})
			return HttpResponse(json_data, content_type="application/json")
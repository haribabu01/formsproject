from django import forms
from productsapp.models import ProductModel

class ProductForm(forms.ModelForm):
	class Meta:
		model = ProductModel
		fields = "__all__"

	# Custom Validation
	def clean_price(self):
		price = self.cleaned_data["price"]
		if price >= 1000:
			return price
		else:
			raise forms.ValidationError("Price is Mininimum of Rs:1000")
from django.forms import ModelForm
from .models import Product

# NOTE: the naming convention shows that methods start with lower-case and classes start with upper-case.

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # NOTE: What that does is grab all the fields within our product and pass that in
        # within this form.

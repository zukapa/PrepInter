from django.shortcuts import render, redirect
from . import models, forms


def get_context_data(request):
    form = forms.ProductsForm()
    model = models.Products
    context = {'table': model.objects.all(),
               'product_name': form.fields['name'].label,
               'product_date': form.fields['date_rec'].label,
               'product_price': form.fields['price'].label,
               'product_u_measure': form.fields['u_measure'].label,
               'product_provider': form.fields['name_provider'].label,
               }
    return render(request, 'goods_list.html', context=context)


def insert_form(request):
    form = forms.ProductsForm()
    print(form)
    if request.method == 'POST':
        form = forms.ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.ProductsForm()
    return render(request, 'good_create.html', {'form': form})

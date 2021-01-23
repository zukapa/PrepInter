from django.shortcuts import render
from . import models, forms
from django.template.loader import render_to_string
from django.http import JsonResponse


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
    if request.method == 'POST':
        form = forms.ProductsForm(request.POST)
    else:
        form = forms.ProductsForm()
    return save_good_form(request, form, 'good_create.html')


def save_good_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            goods = models.Products.objects.all()
            data['html_good_list'] = render_to_string('goods_list.html', {
                'goods': goods
            })
        else:
            data['form_is_valid'] = False
            context = {'form': form}
            data['html_form'] = render_to_string(template_name, context, request=request)
    else:
        data['form_is_valid'] = False
        context = {'form': form}
        data['html_form'] = render_to_string(template_name, context, request=request)
        print(data)

    return JsonResponse(data)

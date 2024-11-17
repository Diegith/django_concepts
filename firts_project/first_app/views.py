from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class CarListView(TemplateView):
    template_name = "first_app/car_list.html"

    def get_context_data(self):
        car_list =[
            {'title': 'Ferrari'},
            {'title': 'Toyota'}, 
            {'title': 'BMW'}         
        ]        
        return {
            'car_list': car_list
        }

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

from django.shortcuts import render
from .forms import CombineSaveForm
from django.views.generic import View
import pandas as pd
from django.shortcuts import redirect
from .models import Category, SubCategory
from django.contrib import messages

# Create your views here.

def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('upload_file')
        data_file = pd.ExcelFile(upload_file)
        cat_data_file = pd.read_excel(data_file , "category")

        sub_data_file = pd.read_excel(data_file , "subcategory")

        for cat in cat_data_file.values:
            Category.objects.get_or_create(name=cat[1])

        for sub in sub_data_file.values:
            SubCategory.objects.get_or_create(name=sub[1], category_id=sub[0])
        return redirect('/')
    return render(request, 'upload.html')

def search_sub(request):
    if request.method == 'POST':
        cat_id = request.POST.get('cat_id')
        sub_cat_objects = SubCategory.objects.filter(category_id=cat_id)

    return render(request, 'sub_result.html', {'sub_categories':sub_cat_objects })


class CombineSaveView(View):

    def post(self, request):
        form = CombineSaveForm(request.POST)
        if form.is_valid():
            
            post = form.save()
            messages.info(request, "Data Saved.")
            return redirect('/')
        return render(request, 'home.html', {'form': form})

    def get(self, request):
        form = CombineSaveForm()
        return render(request, 'home.html', {'form': form})
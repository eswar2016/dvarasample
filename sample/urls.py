from django.urls import path, include
from .views import *

urlpatterns = [
    path('', CombineSaveView.as_view(), name='home' ),
    path('upload', upload, name='upload' ),
    path('find-sub', search_sub, name='search')


]

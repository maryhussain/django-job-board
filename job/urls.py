from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.job_list.as_view(),name= 'list_job'),
    path('<int:id>',views.job_list.as_view(),name= 'list_job'),

]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_form, name= 'emp_insert'), #get and post request of insert operation
    path('list/',views.employee_list, name= 'emp_list'),#get request for retrive and display all records
    path('<int:id>/',views.employee_form, name='emp_update'), #get and post request for update operation
    path('delete/<int:id>/',views.employee_delete, name= 'emp_delete'),

]

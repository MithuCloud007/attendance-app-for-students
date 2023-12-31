from django.urls import path
from department.views import AddDeparment,AllDeparment,ViewDeparment,DeleteDeparment,UpdateDeparment

app_name='department'

urlpatterns = [
    path('department-add', AddDeparment.as_view(), name="department_add"),
    path('department-all', AllDeparment.as_view(), name="department_all"),
    path('department-detail/<int:pk>', ViewDeparment.as_view(), name="department_view"),
    path('department-update/<int:pk>', UpdateDeparment.as_view(), name="department_update"),
    path('department-delete/<int:pk>', DeleteDeparment.as_view(), name="department_delete"),

]
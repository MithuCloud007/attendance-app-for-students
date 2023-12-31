from django.urls import path
from .views import AddClass,AllClass,UpdateClass,DeleteClass,ViewClass


app_name='class_app'

urlpatterns = [
    path('class-add', AddClass.as_view(), name="class_add"),
    path('class-all', AllClass.as_view(), name="class_all"),
    path('class-detail/<int:pk>', UpdateClass.as_view(), name="class_view"),
    path('class-update/<int:pk>', ViewClass.as_view(), name="class_update"),
    path('class-delete/<int:pk>', DeleteClass.as_view(), name="class_delete")
]
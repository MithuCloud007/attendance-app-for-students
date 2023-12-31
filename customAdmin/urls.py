from django.urls import path

from customAdmin.views import backend,login_view,logoutuser

app_name='customAdmin'

urlpatterns = [
	path('', backend, name="backend_dashboard"),
    path('login/', login_view, name='login_page'),
    path('logout/', logoutuser, name='logout_page'),
]
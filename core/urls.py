
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from customAdmin import urls as custom_urls
from department import urls as dept_urls
from attendance import urls as attendance_url
from student import urls as student_urls
from class_app import urls as class_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(custom_urls, namespace='customAdmin')),
    path('', include(dept_urls, namespace='department')),
    path('', include(attendance_url, namespace='attendance')),
    path('', include(student_urls, namespace='student')),
    path('', include(class_app_urls, namespace='class'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
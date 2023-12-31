from django.urls import path

from attendance.views import AttendanceListCreateView,ViewAttendance

app_name='attendance'

urlpatterns = [
	path('attendance', AttendanceListCreateView.as_view(), name="attendance_all"),
    path('attendance-view/<int:pk>/', ViewAttendance.as_view(), name="attendance_view")
]
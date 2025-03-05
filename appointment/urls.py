from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'doctor_type_crud_view_set', views.DoctorTypeCrudViewSet, basename='doctor_type_crud_view_set')
router.register(r'doctor_name_crud_view_set', views.DoctorNameCrudViewSet, basename='doctor_name_crud_view_set')
router.register(r'appointment_date_crud_view_set', views.AppointmentDateCrudViewSet, basename='appointment_date_crud_view_set')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path("", views.MainPage.as_view(), name="main_page"),
#     path('admin_page/', views.AdminPage.as_view(), name='admin_page'),
#     path('login/', views.UserLoginView.as_view(), name='login'),
#     path('user_registration/', views.UserRegisterView.as_view(), name='user_registration'),
#     path('user_logout/', views.UserLogoutView.as_view(), name='user_logout'),
#     path('doctor/', views.CreateDoctorView.as_view(), name='doctor'),
#     path('specialization/', views.CreateDoctorTypeView.as_view(), name='specialization'),
#     path('appointment_date/', views.AppointmentDatesView.as_view(), name='appointment_date'),
#     path('doctor_visit/', views.DoctorTypeSelectView.as_view(), name='doctor_visit'),
#     path('choose_doctor_name/<int:pk>', views.DoctorNameSelectView.as_view(), name='choose_doctor_name'),
#     path('choose_visit_date_time/<int:pk>', views.VisitDateSelectView.as_view(), name='choose_visit_date_time'),
#     path('visit_confirmation/<int:pk>', views.ConfirmAppointmentView.as_view(), name='visit_confirmation'),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from django.contrib.auth.views import LogoutView, LoginView

from . import views

# główne routery
router = DefaultRouter()
router.register(r'doctor_types', views.DoctorTypeViewSet, basename='doctortype')
# router.register(r'doctor_types', views.DoctorTypeCrudViewSet, basename='doctortype')
router.register(r'doctor_names', views.DoctorNameCrudViewSet, basename='doctorname')
router.register(r'appointments', views.AppointmentDateCrudViewSet, basename='appointmentdates')

# nested routers
doctor_nested_router = NestedDefaultRouter(router, r'doctor_types', lookup='doctor_type')
doctor_nested_router.register(r'doctors', views.DoctorNameNestedViewSet, basename='doctortype-doctor')

urlpatterns = [
    # path('', views.HomeView.as_view(), name='hello'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('hellologin/', views.HomeLoginView.as_view(), name='hellologin'),
    # path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('', include(doctor_nested_router.urls)),
    path('api-auth/', include('rest_framework.urls')), # wejdz na 'http://127.0.0.1:8000/api-auth/login/' lub 'http://127.0.0.1:8000/api-auth/logout/'
]

from django.urls import path
from .views import Say, SubmitUserDetails, SubmitDoctorDetails

urlpatterns = [
    path('', Say.as_view(), name='say'),
    path('submit_user_details/', SubmitUserDetails.as_view(), name='submit_user_details'),
    path('submit_doctor_details/', SubmitDoctorDetails.as_view(), name='submit_doctor_details'),
]

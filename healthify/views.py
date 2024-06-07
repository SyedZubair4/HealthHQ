from django.shortcuts import render, redirect
from .models import UserDetails, DoctorDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class Say(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Hello, world!'}, status=status.HTTP_200_OK)

@method_decorator(csrf_exempt, name='dispatch')
class SubmitUserDetails(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        user_details = UserDetails.objects.create(
            full_name=data.get('fullname'),
            age=data.get('age'),
            gender=data.get('gender'),
            phone_number=data.get('phoneNumber'),
            current_medications=data.get('currentMedications'),
            ALLERGIES=data.get('allergies'),
            past_medical_condition=data.get('pastMedicalCondition'),
            blood_type=data.get('bloodType'),
            recent_test_details=data.get('recentTestDetails'),
            food_type=data.get('foodType'),
            address=data.get('address')
        )
        user_details.save()
        return Response({'message': 'User details submitted successfully'}, status=status.HTTP_201_CREATED)

@method_decorator(csrf_exempt, name='dispatch')
class SubmitDoctorDetails(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        doctor_details = DoctorDetails.objects.create(
            fullname=data.get('fullname'),
            age=data.get('age'),
            gender=data.get('gender'),
            blood_type=data.get('bloodType'),
            phone_number=data.get('phoneNumber'),
            adhaar_number=data.get('adhaarNumber'),
            MIDICAL_LICENCE_NO=data.get('medicalLicenceNumber'),
            specialization=data.get('specialization'),
            food_type=data.get('foodType'),
            years_of_experience=data.get('yearsOfExperience')
        )
        doctor_details.save()
        return Response({'message': 'Doctor details submitted successfully'}, status=status.HTTP_201_CREATED)

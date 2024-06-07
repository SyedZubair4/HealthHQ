from django.shortcuts import render, redirect
from .models import UserDetails, DoctorDetails, userRequestForDoctor
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import LoginSerializer

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


@method_decorator(csrf_exempt, name='dispatch')
class userRequestingDoctor(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data = request.data
        requestedDoctor = userRequestForDoctor.objects.create(
            state = data.get('state'),
            city = data.get('city'),
            pincode = data.get('pincode'),
            specialization = data.get('specialization')
        )

        requestedDoctor.save()
        return Response({'message':'Requested for respective doctor successfully','requested':data.get('specialization')},status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import CustomUser, Membership, Document, SavingsPlan, Contribution, AuditLog
from .serializers import (
    RegistrationSerializer,
    MembershipSerializer,
    DocumentSerializer,
    SavingsPlanSerializer,
    ContributionSerializer,
    AuditLogSerializer,
)

from django.core.mail import send_mail
from django_otp.plugins.otp_email.models import EmailDevice
import random

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RegistrationView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             # Generate OTP
#             otp = str(random.randint(100000, 999999))
            
#             # Send OTP via email or SMS (example for email)
#             send_mail(
#                 'Your OTP Code',
#                 f'Your OTP code is: {otp}',
#                 'no-reply@example.com',
#                 [user.email],
#                 fail_silently=False,
#             )


#             return Response({'message': 'User registered successfully! Please check your phone or email for the OTP.'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class SavingsPlanViewSet(viewsets.ModelViewSet):
    queryset = SavingsPlan.objects.all()
    serializer_class = SavingsPlanSerializer


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer


class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer

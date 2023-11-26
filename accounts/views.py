# your_app_name/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer,CreateUserSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self, *args, **kwargs):
        method = self.request.method.lower()
        return UserSerializer if method in ('get', 'delete') else CreateUserSerializer


    def perform_create(self, serializer):
        user = serializer.save()
        self.send_verification_email(user)


    def send_verification_email(self, user):
        subject = 'Email Verification'
        message = f'Thank you for registering. Please click the link below to verify your email.\n\n{self.get_verification_link(user)}'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['paarasarora2@gmail.com']
        send_mail(subject, message, from_email, to_email)

    def get_verification_link(self, user):
        token = default_token_generator.make_token(user)
        return f'http://your_frontend_verification_url/?token={token}'

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            # You can customize the response as needed
            return Response({'token': user.auth_token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



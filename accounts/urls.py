
from django.urls import path
from .views import SignUpView, LoginView,EmailVerificationView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify/<str:token>/', EmailVerificationView.as_view(), name='email-verification')
]
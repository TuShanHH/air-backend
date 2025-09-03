from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('register/', register, name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

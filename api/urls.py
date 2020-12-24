from django.urls import path
from .views.counselor_views import Counselors, CounselorDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('counselors/', Counselors.as_view(), name='counselors'),
    path('counselors/<int:pk>/', CounselorDetail.as_view(), name='counselor_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]

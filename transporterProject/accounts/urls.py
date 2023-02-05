# accounts' urls.py
from django.urls import path, include

from transporterProject.accounts.views import RegistrationView, LogInView, LogOutView, TransporterDetailsView, \
    TransporterEditView, TransporterDeleteView

# SignUpView, SignOutView, \ UserDetailsView, UserEditView, UserDeleteView

urlpatterns = (
    path('register/', RegistrationView.as_view(), name='register transporter'),
    path('login/', LogInView.as_view(), name='login transporter'),
    path('logout/', LogOutView.as_view(), name='logout transporter'),
    path('profile/<int:pk>/', include([
        path('', TransporterDetailsView.as_view(), name='details transporter'),
        path('edit/', TransporterEditView.as_view(), name='edit transporter'),
        path('delete/', TransporterDeleteView.as_view(), name='delete transporter'),
    ])),
)

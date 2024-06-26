from django.urls import path
from .views import SignupView, LoginView, admin_only_view, CRLAvailInstiView, CatAvailInstiView, Branches


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin-view/', admin_only_view, name='admin-view'),
    path('crlavailinsti/', CRLAvailInstiView.as_view(), name='crlavailinsti'),
    path('catavailinsti/', CatAvailInstiView.as_view(), name='catavailinsti'),
    path('branches/', Branches.as_view(), name='branches'),
]
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts.views import SignUp,CreateProfile,DetailProfile,VerifyProfile
app_name= 'accounts'

urlpatterns = [
    url(r'^login/$',auth_views.LoginView.as_view(template_name= 'accounts/login.html'),name= 'login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name = 'logout'),
    url(r'^signup/$',SignUp.as_view(),name = 'signup'),
    url(r'^(?P<username>[-\w\d]+)/profile/create', CreateProfile.as_view(), name='createprofile'),
    url(r'^(?P<username>[-\w]+)/profile/(?P<pk>\d+)/', DetailProfile.as_view(), name='profile'),
    url(r'^(?P<username>[-\w]+)/profile/',VerifyProfile , name='verifyprofile'),
]

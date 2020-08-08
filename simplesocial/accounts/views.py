from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import  TemplateView,CreateView, DetailView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class CreateProfile(LoginRequiredMixin,CreateView):
    model = Profile
    fields = ('contact','gender','profile_pic')
    template_name = 'Profile/profile_form.html'

    def form_valid(self, form):
        if Profile.objects.filter(user = self.request.user).exists():
            return redirect('accounts:profile', username=self.request.user.username,pk=Profile.objects.filter(user = self.request.user)[0].pk)
        profile = form.save(commit=False)
        profile.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        username = self.kwargs.get('username')
        pk = self.object.pk
        return reverse_lazy('accounts:profile', kwargs={'username':username,'pk':pk})

class DetailProfile(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'Profile/profile_detail.html'

def VerifyProfile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
    except:
        if request.user.username == username:
            return redirect('accounts:createprofile', username=username)
        else:
            return render(request,'Profile/profile_not_updated.html',{'username':username})
    return redirect('accounts:profile', username=username,pk=profile.pk)

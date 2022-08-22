from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib import messages
from django.http import HttpResponseRedirect


from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = ProfileUpdateForm
    template_name = 'profile-update.html'

    def post(self, request):

        post_data = request.POST or None

        user_form = ProfileUpdateForm(post_data, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
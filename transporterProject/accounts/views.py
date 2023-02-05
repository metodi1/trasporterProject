from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model

from transporterProject.accounts.forms import TransporterCreateForm, TransporterLogInForm

# Always get the *user model* with `get_user_model`
UserModel = get_user_model()


class RegistrationView(views.CreateView):
    model = UserModel
    form_class = TransporterCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home page')


class LogInView(auth_views.LoginView):
    form_class = TransporterLogInForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home page')


class LogOutView(auth_views.LogoutView):
    next_page = reverse_lazy('home page')


class TransporterEditView(views.UpdateView):
    template_name = 'accounts/transporter-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'profile_image')

    def get_success_url(self):
        return reverse_lazy('details transporter', kwargs={
            'pk': self.request.user.pk,
        })


class TransporterDetailsView(views.DetailView):
    template_name = 'accounts/transporter-user-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        return context


#


class TransporterDeleteView(views.DeleteView):
    template_name = 'accounts/transporter-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('home page')

from allauth.account.views import LoginView as AllAuthLoginView


# Create your views here.
class LoginView(AllAuthLoginView):
    template_name = 'accounts/login.html'

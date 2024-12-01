from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return True


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        raise PermissionDenied("회원가입은 지원되지 않음")

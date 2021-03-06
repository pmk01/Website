from django.views.generic.edit import UpdateView
from django.views.generic import DetailView, RedirectView
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.utils.http import is_safe_url

from ratelimit.mixins import RatelimitMixin

from .models import Member
from .forms import MemberUpdateForm

class MemberLinkRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = reverse(kwargs['url'])
        if is_safe_url(url):
            self.request.session['is_member'] = True
            return url


class MemberMixin():
    def get_object(self, queryset=None):
        if queryset is None:
                queryset = self.get_queryset()

        try:
            member = self.request.user.member
        except Member.DoesNotExist:
            member = Member(user=self.request.user)
            member.save()

        self.member = member
        return member


class MemberLoginFromTokenView(RatelimitMixin, RedirectView):
    ratelimit_key = 'ip'
    ratelimit_rate = '5/m'
    ratelimit_block = True
    ratelimit_method = 'GET'

    def get_redirect_url(self, *args, **kwargs):
        token = kwargs['token']
        user = authenticate(token=token)
        login(self.request, user)
        if self.request.GET.get('edit'):
            return reverse('edit_member')
        return reverse('view_member')


class MemberUpdateView(MemberMixin, UpdateView):
    """
    Take a token and find a Member object that matches it.

    Render an update form for Member object.
    """
    template_name = 'dc_members/edit.html'
    queryset = Member.objects.all()
    slug_url_kwarg = "token"
    slug_field = "token"
    form_class = MemberUpdateForm

    def get_context_data(self, **kwargs):
        context = super(MemberUpdateView, self).get_context_data(**kwargs)

        linked_accounts = {}
        for account in self.member.user.socialaccount_set.all():
            linked_accounts[account.get_provider_display()] = account
        context['linked_accounts'] = linked_accounts

        return context


class MemberHomeView(MemberMixin, DetailView):
    """
    Page for displaying a single member
    """
    template_name = 'dc_members/detail.html'
    queryset = Member.objects.all()
    slug_field = 'token'
    slug_url_kwarg = "token"

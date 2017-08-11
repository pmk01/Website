from django.conf.urls import include, url

from dc_signup_form.forms import MailingListSignupForm
from dc_signup_form.views import SignupFormView

urlpatterns = [
    url(
        r'^signup/$',
        SignupFormView.as_view(
            template_name='base.html',
            form_class=MailingListSignupForm,
            backend='local_db'
        ),
        name='mailing_list_signup_view'),
    url(r'^api_signup/', include('dc_signup_form.signup_server.urls')),
]

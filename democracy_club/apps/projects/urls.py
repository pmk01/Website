from django.conf.urls import url
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    url(
        r"^$",
        TemplateView.as_view(template_name="projects/projects_home.html"),
        name="home",
    ),
    url(
        r"^past/$",
        TemplateView.as_view(template_name="projects/past.html"),
        name="past",
    ),
    url(
        r"^reports/$",
        TemplateView.as_view(template_name="projects/reports_home.html"),
        name="reports",
    ),
    url(
        r"^reports/registers/$",
        TemplateView.as_view(
            template_name="projects/report_odi_registers.html"
        ),
        name="reports_registers",
    ),
    url(
        r"^polling-stations/$",
        TemplateView.as_view(
            template_name="projects/polling-stations/home.html"
        ),
        name="polling_one_pager",
    ),
    url(
        r"^polling-stations/technical/$",
        RedirectView.as_view(url=reverse_lazy("polling_data_upload")),
        name="polling_technical_explainer",
    ),
    url(
        r"^projects/polling-stations/faqs/$",
        RedirectView.as_view(url=reverse_lazy("polling_one_pager")),
        name="polling_faqs",
    ),
    url(
        r"^polling-stations/embed/$",
        TemplateView.as_view(
            template_name="projects/polling-stations/embed_code.html"
        ),
        name="polling_embed_code",
    ),
    url(
        r"^polling-stations/upload/$",
        TemplateView.as_view(
            template_name="projects/polling-stations/upload_data.html"
        ),
        name="polling_data_upload",
    ),
    url(
        r"^polling-stations/techincal/$",
        RedirectView.as_view(url=reverse_lazy("polling_technical_explainer")),
    ),
    url(
        r"^election-ids/reference/$",
        RedirectView.as_view(
            url="https://elections.democracyclub.org.uk/reference_definition"
        ),
        name="election_ids_reference",
    ),
    url(
        r"^election-ids/$",
        TemplateView.as_view(template_name="projects/election-ids.html"),
        name="election_ids",
    ),
    url(
        r"^(?i)who-can-i-vote-for/$",
        TemplateView.as_view(template_name="projects/whocanivotefor.html"),
        name="whocanivotefor",
    ),
    url(
        r"^election-widget/$",
        TemplateView.as_view(template_name="projects/election-widget.html"),
        name="election_widget",
    ),
    url(
        r"^candidates-wiki/$",
        TemplateView.as_view(template_name="projects/candidates.html"),
        name="candidates",
    ),
    url(
        r"^data/$",
        TemplateView.as_view(template_name="projects/data.html"),
        name="data",
    ),
    url(
        r"^(?i)election-leaflets/$",
        TemplateView.as_view(template_name="projects/electionleaflets.html"),
        name="election_leaflets",
    ),
    url(
        r"^(?i)csv/$",
        TemplateView.as_view(template_name="projects/cvs.html"),
        name="cvs",
    ),
]

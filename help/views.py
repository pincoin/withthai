from django.views import generic


class GuideView(generic.TemplateView):
    template_name = 'help/guide.html'


class AboutView(generic.TemplateView):
    template_name = 'help/about.html'


class TermsView(generic.TemplateView):
    template_name = 'help/terms.html'


class PrivacyView(generic.TemplateView):
    template_name = 'help/privacy.html'

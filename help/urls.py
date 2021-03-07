from django.urls import path

from . import views

app_name = 'help'

urlpatterns = [
    path('guide/',
         views.GuideView.as_view(), name='guide'),

    path('about/',
         views.AboutView.as_view(), name='about'),

    path('terms/',
         views.TermsView.as_view(), name='terms'),

    path('privacy/',
         views.PrivacyView.as_view(), name='privacy'),
]

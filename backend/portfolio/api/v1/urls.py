from django.urls import path, include

from portfolio.api.v1 import cases_api, podcast_api
from rest_framework import routers

router = routers.DefaultRouter()

router.register('cases', cases_api.CasesList, basename='cases_list')
router.register('podcasts', podcast_api.PodcastsList, basename='podcasts_list')

urlpatterns = [
    path('', include(router.urls))
]

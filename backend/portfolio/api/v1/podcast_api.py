from rest_framework import mixins, viewsets

from .serializers import PodcastSerializer

from portfolio.models.podcasts import Podcasts


class PodcastsList(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Podcasts.objects.prefetch_related('podcast_link')
    serializer_class = PodcastSerializer

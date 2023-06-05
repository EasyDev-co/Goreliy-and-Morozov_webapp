from config.celery import BaseTask, app
from .models.podcasts import PodcastLink

from django.db import transaction
from pytube import YouTube


class UpdateYouTubeViewsTask(BaseTask):
    autoretry_for = ()

    def proccess(self, *args, **kwargs):
        youtube_podcast_links = PodcastLink.objects.filter(resource=PodcastLink.PodcastType.YOUTUBE)

        with transaction.atomic():
            for podcast_link in youtube_podcast_links:
                new_views = self._get_video_views(url=podcast_link.url)
                podcast_link.podcast.listen_count = new_views
                podcast_link.podcast.save()

    @classmethod
    def _get_video_views(cls, url):
        video_info = YouTube(url=url)
        return video_info.views


update_views_video_task = app.register_task(UpdateYouTubeViewsTask())
app.add_periodic_task(30, update_views_video_task)


# TODO ДОБАВИТЬ в CONTEXT build для норм запуска таски

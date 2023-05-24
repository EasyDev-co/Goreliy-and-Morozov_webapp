from django.db import models


class Podcasts(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    listening_count = models.IntegerField(default=0, verbose_name='Кол-во прослушианий')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(verbose_name='Фото подкаста')

    class Meta:
        db_table = 'podcasts'
        verbose_name = 'Подкаст'
        verbose_name_plural = 'Подкасты'

    def __str__(self):
        return self.title


class PodcastLink(models.Model):

    class PodcastType(models.TextChoices):
        YANDEX = 'YA', 'yandex'
        SPOTIFY = 'SP', 'spotify'
        YOUTUBE = 'YT', 'youtube'

    url = models.URLField(verbose_name='Ссылка на подкаст', max_length=3000)
    resource = models.CharField(
        verbose_name='Ресурс',
        choices=PodcastType.choices,
        max_length=2
    )
    podcast = models.ForeignKey(
        Podcasts,
        verbose_name='Подкаст',
        on_delete=models.CASCADE,
        related_name='podcast_link'
    )

    class Meta:
        db_table = 'podcasts_links'
        verbose_name = 'Ссылка на подкаст'
        verbose_name_plural = 'Ссылки на подкаст'

    def __str__(self):
        return self.url

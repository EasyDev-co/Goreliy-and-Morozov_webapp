from rest_framework import serializers

from portfolio.models.podcasts import Podcasts, PodcastLink
from portfolio.models.cases import (
    Cases,
    CaseTaskText,
    CaseResultText
)


class CasesResultTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseResultText
        fields = '__all__'


class CasesTaskTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseTaskText
        fields = '__all__'


class CasesSerializer(serializers.ModelSerializer):
    case_task_text = CasesTaskTextSerializer(many=True, read_only=True)
    case_result_text = CasesResultTextSerializer(many=True, read_only=True)

    class Meta:
        model = Cases
        fields = [
            'title',
            'desc',
            'image',
            'case_type',
            'case_task_text',
            'case_result_text'
        ]


class PodcastLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = PodcastLink
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    podcast_link = PodcastLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Podcasts
        fields = [
            'title',
            'listening_count',
            'published_at',
            'image',
            'podcast_link'
        ]

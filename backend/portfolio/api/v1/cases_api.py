from rest_framework import mixins, viewsets

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CasesSerializer

from portfolio.models.cases import Cases


class CasesList(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Cases.objects.prefetch_related(
        'case_task_text',
        'case_result_text'
    )
    serializer_class = CasesSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['case_type']

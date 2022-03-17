from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from histories.api.serializer import HistoriesSerializer
from histories.models import Histories


class HistoriesView(viewsets.ModelViewSet):
    serializer_class = HistoriesSerializer

    def get_queryset(self):
        return Histories.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        for h in data:
            h['product'] = h['product']['id']
            history = HistoriesSerializer(data=h)
            if history.is_valid(raise_exception=True):
                history.save()
        return Response(True)

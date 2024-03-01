from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from activities.api.serializers import ArtActivitySerializer
from activities.models import ArtActivity


class ArtActivityViewSet(ModelViewSet):
    queryset = ArtActivity.objects.all()
    serializer_class = ArtActivitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'status']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ArtActivity.objects.all()
        return ArtActivity.objects.filter(user=user)

    def perform_create(self, serializer):
        creator = self.request.user
        if creator.is_superuser:
            super().perform_create(serializer)
        else:
            serializer.save(user=creator, status=ArtActivity.StatusChoices.PENDING)

    def perform_update(self, serializer):
        updater = self.request.user
        if updater.is_superuser:
            super().perform_update(serializer)
        else:
            serializer.save(user=updater, status=self.get_object().status)

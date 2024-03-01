from django.contrib.auth import get_user_model
from rest_framework import serializers

from activities.models import ArtActivity, Photo
from users.api.serializers import UserSerializer

User = get_user_model()


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=False)
    activity = serializers.PrimaryKeyRelatedField(queryset=ArtActivity.objects.all(), required=False, write_only=True)

    class Meta:
        model = Photo
        fields = '__all__'


class ArtActivitySerializer(serializers.ModelSerializer):
    photo_activity = PhotoSerializer(many=True, required=False)

    def to_representation(self, instance):
        request = self.context['request']
        result = super().to_representation(instance)
        result['user'] = UserSerializer(instance.user, context={'request': request}).data
        return result

    def create(self, validated_data):
        photo_activity = validated_data.pop('photo_activity', None)
        instance = super().create(validated_data)
        for i in photo_activity if photo_activity else []:
            Photo.objects.create(image=i.get('image', None), activity=instance)
        return instance

    def update(self, instance, validated_data):
        photo_activity = validated_data.pop('photo_activity', None)
        ids = []
        for i in photo_activity if photo_activity else []:
            id_ = i.get('id', None)
            image_ = i.get('image', None)
            if id_:
                ids.append(id_)
            else:
                photo_obj = Photo.objects.create(image=image_, activity=instance)
                ids.append(photo_obj.id)
        instance.photo_activity.exclude(id__in=ids).delete()
        return super().update(instance, validated_data)

    class Meta:
        model = ArtActivity
        fields = '__all__'

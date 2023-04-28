from rest_framework.serializers import ModelSerializer

from apps.canban.models import Board


class BoardListSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'description'] # columns
        # todo column nested serializer for columns field

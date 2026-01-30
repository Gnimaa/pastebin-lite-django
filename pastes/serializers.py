from rest_framework import serializers
from .models import Paste

class PasteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        fields = ['id', 'content', 'expires_at', 'max_views']


class PasteViewSerializer(serializers.ModelSerializer):
    expired = serializers.SerializerMethodField()

    class Meta:
        model = Paste
        fields = ['content', 'expired']

    def get_expired(self, obj):
        return obj.is_expired()

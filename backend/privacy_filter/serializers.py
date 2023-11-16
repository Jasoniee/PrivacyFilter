from rest_framework import serializers
from .models import PF

class PFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PF
        fields = ('id', 'title', 'description', 'completed')
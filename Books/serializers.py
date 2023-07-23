from rest_framework import serializers
from .models import Books

# I write this example for 5 MB size limit for you
MAX_UPLOAD_SIZE = "52"

class BookSerializer(serializers.ModelSerializer):
    publisher=serializers.CharField(source='publisher.username',read_only=True)
    class Meta:
        model=Books
        fields='__all__'
        read_only_fields=('publisher',)

    def create(self, validated_data):
        validated_data['publisher']=self.context['request'].user
        return Books.objects.create(**validated_data)
    
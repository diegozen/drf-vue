from rest_framework import serializers
from .models import Note, User, Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TagsRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        tag, created = Tag.objects.get_or_create(text=data)
        return tag

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        depth=1

class NoteCreateUpdateSerializer(serializers.ModelSerializer):
    tags = TagsRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Note
        fields = '__all__'
    
    

        


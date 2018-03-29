from rest_framework import serializers
from .models import Tag, Filter

class TagSerializer(serializers.ModelSerializer):
    children = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Tag
        fields = ('id', 'parent', 'children', 'name', 'values', 'filters', 'negate_conditional')


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = ('id', 'tag', 'type_conditional', 'conditional')
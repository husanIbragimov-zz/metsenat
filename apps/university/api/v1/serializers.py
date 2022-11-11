from rest_framework import serializers

from apps.university.models import OTM


class SubOTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTM
        fields = ('id', 'title')


class OTMSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        qs = OTM.objects.filter(parent_category=obj, is_active=True)
        sz = SubOTMSerializer(qs, many=True)
        return sz.data

    class Meta:
        model = OTM
        fields = (
            'id',
            'title',
            'children'
        )

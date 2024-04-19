from rest_framework import serializers
from apps.route.models import Routes


class RoutesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number_route = serializers.CharField(max_length=10)
    name_route = serializers. CharField(max_length=100)

    def create(self, validated_data):
        return Routes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number_route = validated_data.get('number_route', instance.number_route)
        instance.name_route = validated_data.get('name_route', instance.name_route)
        instance.type_trans = validated_data.type_trans('type_trans', instance.type_trans)
        instance.save()
        return instance


class RoutesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = ['id', 'number_route', 'name_route']

from rest_framework import serializers

from .models import *



class GGField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return value.name or None

    def to_internal_value(self, data):
        if self.pk_field is not None:
            data = self.pk_field.to_internal_value(data)
        try:
            return self.get_queryset().get(pk=data)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)

class TestSerializer(serializers.ModelSerializer):
    gg = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=GG.objects.all(), required=False)
    class Meta:
        model = Test
        fields = "__all__"
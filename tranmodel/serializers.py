from rest_framework.serializers import ModelSerializer
from modeltranslation.manager import get_translatable_fields_for_model
from django.conf import settings

from .models import *



class ModelSerializerTranslated(ModelSerializer):
    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        translated_fields = get_translatable_fields_for_model(self.Meta.model)
        languages = settings.LANGUAGES
        translated_fields_with_lang = [f"{field}_{language[0]}" for field in translated_fields for language in languages]
        self.Meta.extra_kwargs = {} if not hasattr(self.Meta, 'extra_kwargs') else self.Meta.extra_kwargs

        for field in translated_fields:
            exist_kwargs = self.Meta.extra_kwargs.get(field)
            exist_kwargs = exist_kwargs if exist_kwargs else {}

            self.Meta.extra_kwargs[field] = exist_kwargs
            self.Meta.extra_kwargs[field]['read_only'] = True

        for field in translated_fields_with_lang:
            exist_kwargs = self.Meta.extra_kwargs.get(field)
            exist_kwargs = exist_kwargs if exist_kwargs else {}
            
            self.Meta.extra_kwargs[field] = exist_kwargs
            self.Meta.extra_kwargs[field]['write_only'] = True

        return fields

    class Meta:
        model = Person
        fields = "__all__"
        
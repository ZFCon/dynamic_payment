from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Person)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
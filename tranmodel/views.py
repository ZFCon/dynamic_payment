from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class PersonViewSet(ModelViewSet):
    serializer_class = ModelSerializerTranslated
    queryset = Person.objects.all()
from rest_framework.generics import CreateAPIView

from .models import *
from .serializers import *



class TestView(CreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
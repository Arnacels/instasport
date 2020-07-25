from rest_framework import generics, permissions
from .serializers import TimeTableSerializers
from .models import TimeTableModel


# Create your views here.
class TimeTableListView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = TimeTableModel.objects.all()
    serializer_class = TimeTableSerializers

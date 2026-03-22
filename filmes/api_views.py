from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Filme
from .serializers import FilmeSerializer


class FilmeListApiView(generics.ListAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
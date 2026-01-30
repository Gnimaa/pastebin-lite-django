from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Paste
from .serializers import PasteCreateSerializer, PasteViewSerializer

class PasteCreateView(APIView):
    def post(self, request):
        serializer = PasteCreateSerializer(data=request.data)
        if serializer.is_valid():
            paste = serializer.save()
            return Response({
                "id": str(paste.id),
                "url": f"/api/pastes/{paste.id}"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasteDetailView(APIView):
    def get(self, request, paste_id):
        paste = get_object_or_404(Paste, id=paste_id)

        if paste.is_expired():
            return Response(
                {"error": "Paste expired"},
                status=status.HTTP_410_GONE
            )

        paste.views += 1
        paste.save()

        serializer = PasteViewSerializer(paste)
        return Response(serializer.data)


# Create your views here.

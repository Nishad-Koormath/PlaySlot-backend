from rest_framework import viewsets, permissions, filters
from .models import Turf
from .serializers import TurfSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class TurfViewSet(viewsets.ModelViewSet):
    queryset = Turf.objects.all().order_by('-created_at')
    serializer_class = TurfSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = ['name', 'location', 'description']
    ordering_fields = ['day_price_per_hour', 'night_price_per_hour', 'created_at']
    
    def get_queryset(self):
        user = self.request.user
        owner_only = self.request.query_params.get('owner')
        if owner_only and user.is_authenticated:
            return Turf.objects.filter(owner=user).order_by('-created_at')
        return super().get_queryset()
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
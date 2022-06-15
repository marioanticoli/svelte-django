from rest_framework import viewsets, permissions

from skeleton.models import Template, Section
from skeleton.serializers import TemplateSerializer, SectionSerializer


class TemplateView(viewsets.ModelViewSet):
    """
    API endpoint that allows skeleton to be viewed or edited.
    """
    queryset = Template.objects.all().order_by('-created_at')
    serializer_class = TemplateSerializer
    permission_classes = [permissions.IsAuthenticated]


class SectionView(viewsets.ModelViewSet):
    """
    API endpoint that allows skeleton' sections to be viewed or edited.
    """
    queryset = Section.objects.all().order_by('-created_at')
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticated]

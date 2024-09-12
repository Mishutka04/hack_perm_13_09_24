
from django.shortcuts import render
from rest_framework import generics, viewsets
import docx
from document.utils import generator_file
from .models import AttrTemplate, Template
from .serializers import AttrTemplateSerializer, TemplateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse

class AttrTemplateListView(generics.ListAPIView):
    serializer_class = AttrTemplateSerializer
    queryset = AttrTemplate.objects.all()

    def get_queryset(self, *args, **kwargs):
        if 'pk' in self.kwargs:
            return AttrTemplate.objects.filter(template__pk = self.kwargs['pk'])

class TemplateListView(generics.ListAPIView):
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()


class GenerateFileView(APIView):
    def post(self, request):
        template = Template.objects.filter(pk=request.data['template'])
        print()
        file = template[0].file.open()
        generator_file(file, request.data['data'])
        return FileResponse(open('gfg.docx', 'rb'), filename='gfg.docx')

# Create your views here.

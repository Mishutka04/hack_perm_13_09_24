from django.urls import path

from document import views





app_name = 'document'


urlpatterns = [
path('template/<int:pk>/', views.AttrTemplateListView().as_view()),
path('template/', views.TemplateListView().as_view()),
path('generate_file/', views.GenerateFileView().as_view()),

 ]
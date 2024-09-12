from django.urls import path

from chat_bot import views

app_name = 'chat_bot'


urlpatterns = [
    path("qween/", views.GenerateAnswerAPIView.as_view()),
    path("model/", views.GenerateAnswerModelView.as_view()),
    path("tg/", views.TelegramView.as_view())
    
    
 ]
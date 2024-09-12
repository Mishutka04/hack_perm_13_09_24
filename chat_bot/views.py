from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
#from sentence_transformers import SentenceTransformer
from chat_bot.management.commands.bot import bot
from chat_bot.models import QueryAnswer
#from gradio_client import Client
#from sklearn.metrics.pairwise import cosine_similarity
import os
import asyncio



# Создание эмбеддингов для заголовков и контента
faq_data = QueryAnswer.objects.all()
faq_data_dict = {item.query: item.answer for item in faq_data}
# base_dir = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(base_dir, "models")
# os.makedirs(model_path, exist_ok=True)
# Инициализация модели эмбеддингов
# model = SentenceTransformer('BAAI/bge-m3')
# model.save(model_path)
#model = SentenceTransformer('sberbank-ai/sbert_large_nlu_ru')

# Создание эмбеддингов для заголовков и контента
titles = [item.query for item in faq_data]
contents = [item.answer for item in faq_data]

#title_embeddings = model.encode(titles)
# content_embeddings = model.encode(contents)

#client = Client("https://qwen-qwen1-5-110b-chat-demo.hf.space/")
class GenerateAnswerAPIView(APIView):
    def post(self, request):
        query = request.data['query']
        # Преобразование запроса пользователя в эмбеддинг
        user_query_embedding = model.encode([query])

        # Поиск наиболее релевантного заголовка
        title_similarity_scores = cosine_similarity(user_query_embedding, title_embeddings)
        best_title_idx = title_similarity_scores.argmax()

        # Поиск наиболее релевантного контента
        # content_similarity_scores = cosine_similarity(user_query_embedding, content_embeddings)
        # best_content_idx = content_similarity_scores.argmax()

        # Получение заголовка и контента
        best_match_title = titles[best_title_idx]
        # best_match_content = contents[best_content_idx]
        best_match_content = faq_data_dict.get(best_match_title, None)
        print(best_match_content)

        # if best_match_content is None:
        #     best_match_content = contents[best_content_idx]

        dox = f"Пользователь задал вопрос: '{query}'.Сгенерируйте подробный и полезный ответ исключительно на основании: | Содержание - {best_match_content}' и 'Заголовок - {best_match_title}'."

        result = client.predict(
            dox,  # Вводимый текст
            [["None", "None"], ],  # Начальное состояние чата
            "None",  # Дополнительные параметры
            api_name="/model_chat"
        )
        return Response(
            {
                'fast_result': best_match_content,
                'result': result[1][1][1]
            }
        )




class GenerateAnswerModelView(APIView):
    def post(self, request):
        user_query = request.data['query']
        # Преобразование запроса пользователя в эмбеддинг
        user_query_embedding = model.encode([user_query])

        # Поиск наиболее релевантного заголовка
        title_similarity_scores = cosine_similarity(user_query_embedding, title_embeddings)
        if max(title_similarity_scores[0]) < 0.60:
            return Response({'error': "В моей базе данных нету ответа на ваш вопрос. Попробуйте переформулировать ваш запрос"})
        print(title_similarity_scores)
        best_title_idx = title_similarity_scores.argmax()

        # Получение заголовка и контента
        best_match_title = titles[best_title_idx]
        best_match_content = contents[best_title_idx]
 
        return Response({'title': best_match_title, 'content':best_match_content})
        # Генерация ответа через Gradio
        #response = generate_gradio_answer(best_match_title, best_match_content, user_query)
# Create your views here.
class TelegramView(APIView):
    def post(self, request):
        bot.send_message(1379391469, f"Здорова, брат! Я бот. ")
        return Response({'title': 'D', 'content':3123})
        
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    # def post(self):
    #     a1=Article(title='bhu', auther='bhubhu', cost=1000)
    #     # articles = Article.objects.create(a1)
    #     # print('article',articles)
    #     return Response({"articles": 'hi'})

    # def post(self, request):
    #     # print(request.POST)
    #     # print(request.GET)
    #     article = request.data.get('article')
    #
    #     # Create an article from the above data
    #     serializer = ArticleSerializer(data=article)
    #     # if serializer.is_valid(raise_exception=True):
    #     article_saved = serializer.save()
    #     # return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
    #     return Response({"success": "Article '{}' created successfully"})

    # def post(self, request):
    #     print(request.data)
    #     # article = request.data.get('article')
    #     article = request.data
    #     serializer = ArticleSerializer(data=article)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #         return Response({"success": article_saved})
    #     return Response({"success": "Article '{}' created successfully"})

    def post(self, request):
        article = request.data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            # article_saved = serializer.data.get('title')
            article_saved = serializer.data
            serializer.save()
            return Response({"success": article_saved})
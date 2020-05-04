from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.
# @csrf_exempt
# After importing api_view we dont want more @csrf_exempt

# Next Generic viewset   
class ArticleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin):
    
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer
        # authentication_classes = [TokenAuthentication]
        # permission_classes = [IsAuthenticated]





# class ArticleViewSet(viewsets.ViewSet):

    # def list(self, request):
    #     queryset = Article.objects.all()
    #     serializer = ArticleSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self,request):
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     queryset = Article.objects.all()
    #     article = get_object_or_404(queryset, pk=pk)
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     article = Article.objects.get(pk=pk)
    #     serializer = ArticleSerializer(article,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# Finaly got another one generic class based-views

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



# Not the last step then got mixins
# class ArticleList(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 generics.GenericAPIView):

#             queryset = Article.objects.all()
#             serializer_class = ArticleSerializer

#             def get(self, request, *args, **kwargs):
#                 return self.list(request, *args, **kwargs)

#             def post(self, request, *args, **kwargs):
#                 return self.create(request, *args, **kwargs)

# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):

#                 queryset = Article.objects.all()
#                 serializer_class = ArticleSerializer
                    
#                 def get(self, request, *args, **kwargs):
#                     return self.retrieve(request, *args, **kwargs)

#                 def put(self, request, *args, **kwargs):
#                     return self.update(request, *args, **kwargs)

#                 def delete(self, request, *args, **kwargs):
#                     return self.destroy(request, *args, **kwargs)        


# At last step we making classbased views
# class ArticleList(APIView):

#     def get(self,request,format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self,request,format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                    

# class ArticleDetail(APIView):

#     def get_object(self,pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise Http404

#     def get(self,request,pk,format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self,request,pk,format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk,format=None):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# Making class view am not more using function view

# @api_view(['GET','POST'])
# def article_list(request):

#     if request.method == 'GET':

#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         # @apiview we import response from rest_ so change json_response
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         # @api_view dont want data  
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# @api_view(['GET','PUT','DELETE'])
# def article_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         article = Article.objects.get(pk=pk)
#     except article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
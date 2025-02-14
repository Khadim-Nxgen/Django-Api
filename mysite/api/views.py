from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost
from .serializer import BlogPostSerializer
from rest_framework.views import APIView

class BlogPostListCreate(generics.ListCreateAPIView):
  queryset=BlogPost.objects.all()
  serializer_class=BlogPostSerializer
  def delete(self, request, *args ,**kwargs):
    BlogPost.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDesroy(generics.RetrieveDestroyAPIView):
  queryset=BlogPost.objects.all()
  serializer_class=BlogPostSerializer
  lookup_field="pk"



class BlogPostList(APIView):
  def get(self, request,Format=None):
    title=request.query_params.get("title","")
    if title:
      blog_post=BlogPost.objects.filter(title__icontains=title)

    else:
      blog_post.BlogPost.objects.all()    

    serilizer=BlogPostSerializer(blog_post,many=True)  
    return Response(serilizer.data,status=status.HTTP_204_NO_CONTENT)


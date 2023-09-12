from django.shortcuts import render,get_object_or_404
from .models import KitoblarModel,AvtorlarModel
from rest_framework.views import APIView
from .serializers import KitobSerializer,AvtorlarSerializer
from rest_framework.response import Response
# Create your views here.

class AllKitob(APIView):
    def get(self,request):
        all = KitoblarModel.objects.all()
        serializer = KitobSerializer(all,many = True)
        return Response(serializer.data)

class DetailKitob(APIView):
    def get(self,request,*args,**kwargs):
        detail = get_object_or_404(KitoblarModel,id = kwargs['kitob_id'])
        serializer = KitobSerializer(detail)
        return Response(serializer.data)
    
class CreateKitob(APIView):
    def post(self,request):
        serializer = KitobSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateKitob(APIView):
    def patch(self,request,*args,**kwargs):
        todo = get_object_or_404(KitoblarModel,id=kwargs['kitob_id'])
        serializer = KitobSerializer(todo,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class DeleteKitob(APIView):
    def delete(self,request,*args,**kwargs):
        todo = get_object_or_404(KitoblarModel,id=kwargs['kitob_id'])
        todo.delete()
        return Response('data deleted')
    

class AllAvtor(APIView):
    def get(self,request):
        all = AvtorlarModel.objects.all()
        serializer = AvtorlarModel(all,many=True)
        return Response(serializer.data)
    
class DetailAvtorlar(APIView):
    def get(self,request,*args,**kwargs):
        detail = get_object_or_404(AvtorlarModel,id = kwargs['avtor_id'])
        serializer = AvtorlarSerializer(detail)
        return Response(serializer.data)
    
class CreateAvtorlar(APIView):
    def post(self,request):
        serializer = AvtorlarModel(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class UpdateAvtorlar(APIView):
    def patch(self,request,*args,**kwargs):
        todo = get_object_or_404(AvtorlarModel,id=kwargs['avtor_id'])
        serializer = AvtorlarSerializer(todo,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteAvtorlar(APIView):
    def delete(self,request,*args,**kwargs):
        todo = get_object_or_404(AvtorlarModel,id=kwargs['avtor_id'])
        todo.delete()
        return Response('data deleted')
class get_book(APIView):
    def get(self,*args,**kwargs):
        info = KitoblarModel.objects.filter(id= kwargs['avtor_id'])
        serializer = KitobSerializer(info,many = True)
        return Response(serializer.data)
    
    
    
    

    
    

from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .serializers import p1_method_serializer,p1_method_detail_serializer,avamel_serializer,amel_score_serializer
from .models import p1_methods,avamel,amel_score
# Create your views here.




class total_p1_methods(APIView):
    
    def get(self,request):
        data_total_p1_methods = p1_methods.objects.all()
        serializer = p1_method_serializer(instance=data_total_p1_methods,many=True)
        return Response(data=serializer.data)


class p1_method_detail(APIView):

    def get(self,request,method_id):
        data_p1_method_select = p1_methods.objects.filter(id=method_id).first()
        serializer = p1_method_detail_serializer(instance=data_p1_method_select)
        return Response(data=serializer.data)


class total_p1_method_avamels(APIView):

    def get(self,request):
        total_avamels = avamel.objects.all()
        serializer = avamel_serializer(instance=total_avamels,many=True)
        return Response(data=serializer.data)

    
    def post(self,request):
        serializer = avamel_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)





class p1_method_amel_scores(APIView):

    def get(self,request,method_id,amel_id):
        p1_method_selected = p1_methods.objects.filter(id=method_id).first()
        amel = p1_method_selected.avamels.filter(id=amel_id).first()
        data_method_p1_amel_scores = amel.scores.all()
        serializer = amel_score_serializer(instance=data_method_p1_amel_scores,many=True)
        return Response(data=serializer.data)
        
from django.shortcuts import render,get_object_or_404
from exam.models import  QuestionDb,SubmissionDb
from exam.serializers import QuestionDbSerializer,SubmissionDbSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class QuestionListCreateView(APIView):
    def get(self,request):
        qs=QuestionDb.objects.all()
        serializer_instance=QuestionDbSerializer(qs,many=True)
        return Response(serializer_instance.data)
    def post(self,request):
        form_data=request.data    
        serializer_instance=QuestionDbSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
class QuestionDbRetreveUpdateDeleteView(APIView):
    def get(self,request,pk):
        # qs=QuestionDb.objects.get(id=pk)
        qs=get_object_or_404(QuestionDb,id=pk)
        serializer_instance=QuestionDbSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data

        serializer_instance=QuestionDbSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()
        return Response(data={"message":"Question deleted sucessfuly"})
class SubmissionDbListCreateView(APIView):
    def get(self,request):
        qs= SubmissionDb.objects.all()
        serializer_instance=SubmissionDbSerializer(qs,many=True)
        return Response(serializer_instance.data)
    def post(self,request):
            form_data=request.data    
            serializer_instance=SubmissionDbSerializer(data=form_data)
            if serializer_instance.is_valid():
                actual_data=serializer_instance.validated_data
                SubmissionDb.objects.create(**actual_data)
                return Response(data=serializer_instance.data)
            else:
                return Response(serializer_instance.errors)
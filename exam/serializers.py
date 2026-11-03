from rest_framework import serializers
from exam.models import QuestionDb


class QuestionDbSerializer(serializers.Serializer):
    Question = serializers.CharField(max_length=200)
    option_a = serializers.CharField(max_length=200)
    option_b = serializers.CharField(max_length=200)
    option_c = serializers.CharField(max_length=200)
    option_d = serializers.CharField(max_length=200)
    correct_answer = serializers.CharField(max_length=200)
class SubmissionDbSerializer(serializers.Serializer):
    student_name=serializers.CharField(max_length=100)
    Question_id=serializers.IntegerField()
    Selected_answer=serializers.CharField(max_length=500)
    submitted_at=serializers.DateTimeField(read_only=True)
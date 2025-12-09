from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Member, Trainer, WorkoutSession

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['join_date']

class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Trainer
        fields = '__all__'

class WorkoutSessionSerializer(serializers.ModelSerializer):
    member_detail = MemberSerializer(source='member', read_only=True)
    trainer_detail = TrainerSerializer(source='trainer', read_only=True)
    
    class Meta:
        model = WorkoutSession
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class WorkoutSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = ['member', 'trainer', 'session_date', 'duration_minutes', 'session_type', 'notes']
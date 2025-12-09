from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Member, Trainer, WorkoutSession
from .serializers import (
    UserSerializer, MemberSerializer, TrainerSerializer,
    WorkoutSessionSerializer, WorkoutSessionCreateSerializer
)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для просмотра пользователей
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint для участников клуба
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]

class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint для тренеров
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint для тренировочных сессий
    """
    queryset = WorkoutSession.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return WorkoutSessionCreateSerializer
        return WorkoutSessionSerializer

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """
        Получить предстоящие тренировочные сессии
        """
        from django.utils import timezone
        upcoming_sessions = WorkoutSession.objects.filter(
            session_date__gte=timezone.now(),
            status='scheduled'
        ).order_by('session_date')
        
        page = self.paginate_queryset(upcoming_sessions)
        if page is not None:
            serializer = WorkoutSessionSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = WorkoutSessionSerializer(upcoming_sessions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def member_sessions(self, request):
        """
        Получить тренировочные сессии текущего пользователя (участника)
        """
        try:
            member = request.user.member
            sessions = WorkoutSession.objects.filter(member=member).order_by('-session_date')
            
            page = self.paginate_queryset(sessions)
            if page is not None:
                serializer = WorkoutSessionSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            
            serializer = WorkoutSessionSerializer(sessions, many=True)
            return Response(serializer.data)
        except Member.DoesNotExist:
            return Response(
                {'error': 'User is not a member'},
                status=status.HTTP_400_BAD_REQUEST
            )
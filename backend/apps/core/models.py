from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    """
    Модель участника фитнес-клуба
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    membership_type = models.CharField(
        max_length=50,
        choices=[
            ('standard', 'Стандарт'),
            ('premium', 'Премиум'),
            ('vip', 'VIP'),
        ],
        default='standard'
    )
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-join_date']
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Trainer(models.Model):
    """
    Модель тренера
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trainer')
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-experience_years']
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.specialization}"

class WorkoutSession(models.Model):
    """
    Модель тренировочной сессии (связывает участника и тренера)
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='workout_sessions')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='workout_sessions')
    session_date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=60)
    session_type = models.CharField(
        max_length=50,
        choices=[
            ('personal', 'Персональная'),
            ('group', 'Групповая'),
            ('online', 'Онлайн'),
        ],
        default='personal'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'Запланирована'),
            ('completed', 'Завершена'),
            ('cancelled', 'Отменена'),
            ('in_progress', 'В процессе'),
        ],
        default='scheduled'
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-session_date']
        verbose_name = 'Тренировочная сессия'
        verbose_name_plural = 'Тренировочные сессии'
    
    def __str__(self):
        return f"{self.member} - {self.trainer} - {self.session_date}"
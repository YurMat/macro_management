from django.db import models

# Create your models here.
class DailyIntake(models.Model):
    class Meta:
        db_table = 'daily_intake'

        protain = models.IntergerField(verbose_name='摂取量', max_rength=300)
        Fat = models.IntergerField(verbose_name='脂質', max_rength=300)
        carb = models.IntergerField(verbose_name='炭水化物', max_rength=300)
        filled_at = models.DateTimeField(verbose_name='作成日')

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta(object):
        db_table = 'custom_user'

    login_count = models.IntegerField(verbose_name='ログイン回数', default=0)

    def post_login(self):

        """ログイン後処理"""
        self.login_count += 1
        self.save()
from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(null=False, blank=False, max_length=50)
    user_email = models.EmailField(null=False, blank=False, max_length=50)
    user_password = models.CharField(null=False, blank=False, max_length=50, unique=True)
    user_address = models.TextField(null=False, blank=False)
    user_language = models.CharField(null=False, blank=False, max_length=50)

    class Meta:
        # 테이블명 작성
        db_table = 'tbl_user'

    def __str__(self):
        return self.user_name
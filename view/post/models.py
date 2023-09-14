from django.db import models

from view.models import Period


# Create your models here.
class Post(Period):
    post_title = models.CharField(max_length=200, null=False, blank=False)
    post_content = models.CharField(max_length=500, null=False, blank=False)

    class Meta:
        ordering = ['-id']
        db_table = 'tbl_post'


    # def get_absolute_url(self):
    #     return f"/post/detail/{self.id}"
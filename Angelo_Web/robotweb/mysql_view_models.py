from .models import *

class ArtilceAuthorInfo(models.Model):
    id = models.SmallIntegerField()
    title = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    pub_date = models.DateTimeField()
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s-%s' %(self.title,self.username)

    class Meta :
        db_table = 'article_author_tag'
from django.db import models

class doubanmovie(models.Model):
    title = models.CharField(max_length=50, db_column='title', verbose_name='电影名')
    info = models.CharField(max_length=50, db_column=' info', verbose_name='导演名')
    info_1 = models.CharField(max_length=50, db_column=' info_1', verbose_name='演员名')
    date = models.CharField(max_length=50, db_column='date', verbose_name='上映日期')
    country = models.CharField(max_length=50, db_column=' country', verbose_name='城市')
    geners = models.CharField(max_length=50, db_column=' geners', verbose_name='类型')
    rate = models.CharField(max_length=50, db_column=' rate', verbose_name='分数')
    comCount = models.CharField(max_length=50, db_column=' comCount', verbose_name='评论人数')

    class Meta:
        db_table = 'doubanmovie'
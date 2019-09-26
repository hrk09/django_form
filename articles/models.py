from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 데이터 업데이트 되면 언제든지 해당 시간 추가
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return f'{self.pk} - {self.title}'
    


from django.db import models
# 클래스로써 어떤 데이터의 종류를 처리할지 적는 공간
class Heroku(models.Model):
    title = models.CharField(max_length=200) #title이라는 변수에 짧은 문장(charfield)를 저장한다.
    image = models.ImageField(upload_to='images/')# 정형화된 시간데이터를 사용하겠
    description = models.CharField(max_length=500) #title보다 긴 텍스트 데이터를 사용

    def __str__(self):
        return self.title 
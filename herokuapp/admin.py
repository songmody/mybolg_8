from django.contrib import admin
from .models import Heroku #models폴더에서 Blog라고 하는 객체를 가져와라

admin.site.register(Heroku) #admin사이트에 등록해라
# Register your models here.

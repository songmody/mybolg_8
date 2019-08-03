from django.contrib import admin
from .models import Blog #models폴더에서 Blog라고 하는 객체를 가져와라

admin.site.register(Blog) #admin사이트에 등록해라
# Register your models here.

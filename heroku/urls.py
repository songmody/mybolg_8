from django.contrib import admin
from django.urls import path
import blogapp.views #blogapp에서 값을 view에서 받고 주소만들기
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/<int:blog_id>',blogapp.views.finish,name="finish"),
    path('',blogapp.views.home,name="home"),#home이라는주소생성
    path('blog/drink/',blogapp.views.drink, name="drink"),
    path('blog/food/',blogapp.views.food, name="food"),
    path('blog/fashion/',blogapp.views.fashion, name="fashion"),
    path('blog/specialprice/',blogapp.views.specialprice, name="specialprice"),
    path('blog/message/',blogapp.views.message, name="message"),
    path('blog/create',blogapp.views.create, name="create"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
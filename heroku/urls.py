from django.contrib import admin
from django.urls import path
import herokuapp.views #blogapp에서 값을 view에서 받고 주소만들기
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heroku/<int:blog_id>',heroku.views.finish,name="finish"),
    path('',heroku.views.home,name="home"),#home이라는주소생성
    path('heroku/drink/',heroku.views.drink, name="drink"),
    path('heroku/food/',heroku.views.food, name="food"),
    path('heroku/fashion/',heroku.views.fashion, name="fashion"),
    path('heroku/specialprice/',heroku.views.specialprice, name="specialprice"),
    path('heroku/message/',heroku.views.message, name="message"),
    path('heroku/create',heroku.views.create, name="create"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
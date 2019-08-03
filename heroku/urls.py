from django.contrib import admin
from django.urls import path
import herokuapp.views #blogapp에서 값을 view에서 받고 주소만들기
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heroku/<int:heroku_id>',herokuapp.views.finish,name="finish"),
    path('',herokuapp.views.home,name="home"),#home이라는주소생성
    path('heroku/drink/',herokuapp.views.drink, name="drink"),
    path('heroku/food/',herokuapp.views.food, name="food"),
    path('heroku/fashion/',herokuapp.views.fashion, name="fashion"),
    path('heroku/specialprice/',herokuapp.views.specialprice, name="specialprice"),
    path('heroku/message/',herokuapp.views.message, name="message"),
    path('heroku/create',herokuapp.views.create, name="create"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
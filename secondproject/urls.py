from django.contrib import admin
from django.urls import path, include #다른 폴더에 있는 url을 가져오기위해 include를 import
import blog.views
import portfolio.views
#media를 쓰려면 꼭 import해야할 두가지
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home,name="home"),
    path('blog/',include('blog.urls')),
    path('portfolio/',portfolio.views.portfolio,name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

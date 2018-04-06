from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url(r'^$',views.Index,name='index'),
   url(r'^api/products/$', views.ProductList.as_view()),
   url(r'^api/categories/$', views.CategoryList.as_view()),
   url(r'^api-token-auth/', obtain_auth_token),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
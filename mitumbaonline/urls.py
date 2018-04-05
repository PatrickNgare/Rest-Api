from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
   url(r'^api/products/$', views.ProductList.as_view()),
   url(r'^api/categories/$', views.CategoryList.as_view()),
   url(r'^api-token-auth/', obtain_auth_token),

]

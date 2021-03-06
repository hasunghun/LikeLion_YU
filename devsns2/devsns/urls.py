from django.contrib import admin
from django.urls import path
from snsapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    
    # 127.0.0.1:8000/detail/postid(1~)
]

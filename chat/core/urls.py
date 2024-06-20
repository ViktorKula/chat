from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import logout_view, user_page_view, avatar_edit, user_list
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_page/', user_page_view, name='user_page'),
    path('avatar_edit/', avatar_edit, name='avatar_edit'),
    path('username_edit/', views.username_edit, name='username_edit'),
    path('user-list/', views.user_list, name='user-list'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

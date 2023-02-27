"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home
from articles import views as articles_views 
from forms_app.views import get_prompt
from accounts import views as accounts_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view),
    path('register/', accounts_views.register_view),
    path('articles/', articles_views.article_search_view),
    path('articles/create/', articles_views.article_create_view),
    path('articles/<int:id>/', articles_views.article_detail_view),
    path('', home),
    path('openai/', get_prompt),
    
]

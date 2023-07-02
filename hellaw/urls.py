from django.contrib import admin
from django.urls import path, include
#from social_django.views import auth, complete, social_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hellawapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    # path('oauth/login/kakao/', auth, name='kakao_login'),
    # path('oauth/complete/kakao/', complete, name='kakao_complete'),
    
]

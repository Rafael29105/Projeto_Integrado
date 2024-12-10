from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('menu/', include('menu.urls')),
    path('orders/', include('orders.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('carrinho/', include('carrinho.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
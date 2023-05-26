from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns (
    path('', include('shop_app.urls')),

)

urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)



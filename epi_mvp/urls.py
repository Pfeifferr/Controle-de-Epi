from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("colaboradores/", include("colaboradores.urls", namespace="colaboradores")),
    path("", lambda r: HttpResponseRedirect("/colaboradores/")),
]

# Servir arquivos estáticos em modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")

from django.contrib.auth import admin
from django.urls import path, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('transporterProject.common.urls')),
                  path('accounts/', include('transporterProject.accounts.urls')),
                  path('statistic/', include('transporterProject.statistic.urls')),
                  # path('pets/', include('petstagram.pets.urls')),
                  # path('photos/', include('petstagram.photos.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

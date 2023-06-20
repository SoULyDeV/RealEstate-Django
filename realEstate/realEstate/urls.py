from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from listings.views import (
    
    listing_list,
    listing_retrieve,
    listing_create,
    listing_uptdate,
    listing_delete,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listing/<pk>/', listing_retrieve),
    path('listing/<pk>/edit/', listing_uptdate),
    path('listing/<pk>/delete/', listing_delete),
    path('add_listing/', listing_create),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    
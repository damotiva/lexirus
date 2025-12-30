from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

from lexirus.controllers import general_controller

urlpatterns = [

    # New Document Translation Task
    path('new/document/translation/task', general_controller.upload_input_document),



]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
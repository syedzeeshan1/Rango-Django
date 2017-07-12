from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
from registration.backends.simple.views import RegistrationView
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'
urlpatterns = [

url(r'^rango/', include('rango.urls')),
url(r'^admin/', admin.site.urls),
url(r'^accounts/', include('registration.backends.simple.urls')),
url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


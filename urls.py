from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
     (r'^slot/(?P<slot_id>[^/]+)/show/$', views.slotshow),
)
from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
     url(r'^slot/(?P<slot_id>[^/]+)/show/$', views.slotshow, name='banners_slotshow'),
)
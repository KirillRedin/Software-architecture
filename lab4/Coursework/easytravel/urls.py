from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from easytravel import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^hotels/$', views.HotelList.as_view()),
    url(r'^hotels/(?P<pk>[0-9]+)/$', views.HotelDetail.as_view()),
    url(r'^apartments/$', views.ApartmentList.as_view()),
    url(r'^apartments/(?P<pk>[0-9]+)/$', views.ApartmentDetail.as_view()),
    url(r'^bookings/$', views.BookingList.as_view()),
    url(r'^bookings/(?P<pk>[0-9]+)/$', views.BookingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='restframework')),
]
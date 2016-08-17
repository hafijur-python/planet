from django.conf.urls import url
from.import views


urlpatterns=[

	# url(r'^planets$', views.planets, name="planets"),

	# url(r'^(?P<id>[0-9]+)/$', views.planet_detail, name='planet_detail'),
 #    url(r'^addplanet$', views.addplanet, name="addplanet"),
   
	url(r'^file/$', views.file_create, name="file_create"),
   url(r'^description/$', views.description, name="description"),
   url(r'^(?P<id>[0-9]{1})/$', views.single, name="single"),
   # url(r'^p(?P<i>[0-9])/$', views.single, name='single'),
]	
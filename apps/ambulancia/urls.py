from django.conf.urls import url, patterns

urlpatterns = patterns('apps.ambulancia.views',
    url(r'^$', 'index', name='index'),
    url(r'^presentismo/$', 'presentismo', name='presentismo'),
    # Pasajeros
    url(r'^pasajero/$', 'list_pasajeros', name='list_pasajero'),
    url(r'^pasajero/new/$', 'new_pasajero', name='new_pasajero'),
    url(r'^pasajero/(?P<id>[0-9]+)/delete/$',
         'delete_pasajero', name='delete_pasajero'),
    url(r'^pasajero/(?P<id>[0-9]+)/edit/$',
         'edit_pasajero', name='edit_pasajero'),

    # Establecimientos
    url(r'^establecimiento/new/$', 'new_establecimiento',
         name='new_establecimiento'),

    # Obras Sociales
    url(r'obrasocial/new/$', 'new_obra_social', name='new_obra_social')
    )
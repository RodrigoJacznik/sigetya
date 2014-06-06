from django.conf.urls import url, patterns

urlpatterns = patterns('apps.gestion_pasajeros.views',
    url(r'^$', 'index', name='index'),
    url(r'^asistencia/$', 'asistencia', name='asistencia'),
    url(r'^conformidad/$', 'conformidad', name='conformidad'),
    url(r'^presupuesto/$', 'presupuesto', name='presupuesto'),
    # Pasajeros
    url(r'^pasajero/$', 'list_pasajeros', name='list_pasajero'),
    url(r'^pasajero/new/$', 'new_pasajero', name='new_pasajero'),
    url(r'^pasajero/(?P<id>[0-9]+)/delete/$',
         'delete_pasajero', name='delete_pasajero'),
    url(r'^pasajero/(?P<id>[0-9]+)/edit/$',
         'edit_pasajero', name='edit_pasajero'),

    # Establecimientos
    url(r'^establecimiento/$', 'list_establecimiento',
         name='list_establecimiento'),
    url(r'^establecimiento/new/$', 'new_establecimiento',
         name='new_establecimiento'),


    # Obras Sociales
    url(r'obrasocial/$', 'list_obra_social', name='list_obra_social'),
    url(r'obrasocial/new/$', 'new_obra_social', name='new_obra_social'),

    )
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ObraSocial'
        db.create_table('ambulancia_obrasocial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('precio_km', self.gf('django.db.models.fields.FloatField')()),
            ('precio_ambulancia_dia', self.gf('django.db.models.fields.FloatField')()),
            ('precio_ambulancia_dia_silla', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('ambulancia', ['ObraSocial'])

        # Adding model 'Establecimiento'
        db.create_table('ambulancia_establecimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telefono', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('hora_entrada', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('hora_salida', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('ambulancia', ['Establecimiento'])

        # Adding model 'Pasajero'
        db.create_table('ambulancia_pasajero', (
            ('nro_obra_social', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=20)),
            ('obra_social', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ambulancia.ObraSocial'])),
            ('establecimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ambulancia.Establecimiento'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1, default='M')),
            ('telefono', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre_padre', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('tipo_viaje', self.gf('django.db.models.fields.CharField')(max_length=10, default='AS')),
            ('hora_entrada', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hora_salida', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('ambulancia', ['Pasajero'])


    def backwards(self, orm):
        # Deleting model 'ObraSocial'
        db.delete_table('ambulancia_obrasocial')

        # Deleting model 'Establecimiento'
        db.delete_table('ambulancia_establecimiento')

        # Deleting model 'Pasajero'
        db.delete_table('ambulancia_pasajero')


    models = {
        'ambulancia.establecimiento': {
            'Meta': {'object_name': 'Establecimiento'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hora_entrada': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'hora_salida': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'})
        },
        'ambulancia.obrasocial': {
            'Meta': {'object_name': 'ObraSocial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio_ambulancia_dia': ('django.db.models.fields.FloatField', [], {}),
            'precio_ambulancia_dia_silla': ('django.db.models.fields.FloatField', [], {}),
            'precio_km': ('django.db.models.fields.FloatField', [], {})
        },
        'ambulancia.pasajero': {
            'Meta': {'object_name': 'Pasajero'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'establecimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ambulancia.Establecimiento']"}),
            'hora_entrada': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hora_salida': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_padre': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'nro_obra_social': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '20'}),
            'obra_social': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ambulancia.ObraSocial']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'M'"}),
            'telefono': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'tipo_viaje': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'AS'"})
        }
    }

    complete_apps = ['ambulancia']
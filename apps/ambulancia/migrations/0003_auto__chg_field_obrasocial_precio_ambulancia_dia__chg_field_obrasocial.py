# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ObraSocial.precio_ambulancia_dia'
        db.alter_column('ambulancia_obrasocial', 'precio_ambulancia_dia', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'ObraSocial.precio_km'
        db.alter_column('ambulancia_obrasocial', 'precio_km', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'ObraSocial.precio_ambulancia_dia_silla'
        db.alter_column('ambulancia_obrasocial', 'precio_ambulancia_dia_silla', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'ObraSocial.precio_ambulancia_dia'
        db.alter_column('ambulancia_obrasocial', 'precio_ambulancia_dia', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ObraSocial.precio_km'
        db.alter_column('ambulancia_obrasocial', 'precio_km', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ObraSocial.precio_ambulancia_dia_silla'
        db.alter_column('ambulancia_obrasocial', 'precio_ambulancia_dia_silla', self.gf('django.db.models.fields.FloatField')())

    models = {
        'ambulancia.establecimiento': {
            'Meta': {'object_name': 'Establecimiento'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hora_entrada': ('django.db.models.fields.TimeField', [], {}),
            'hora_salida': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'})
        },
        'ambulancia.obrasocial': {
            'Meta': {'object_name': 'ObraSocial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio_ambulancia_dia': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'precio_ambulancia_dia_silla': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'precio_km': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'ambulancia.pasajero': {
            'Meta': {'object_name': 'Pasajero'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'establecimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ambulancia.Establecimiento']"}),
            'hora_entrada': ('django.db.models.fields.TimeField', [], {}),
            'hora_salida': ('django.db.models.fields.TimeField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_padre': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'nro_obra_social': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '20'}),
            'obra_social': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ambulancia.ObraSocial']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'telefono': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'tipo_viaje': ('django.db.models.fields.CharField', [], {'default': "'AS'", 'max_length': '10'})
        }
    }

    complete_apps = ['ambulancia']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Responsable.dni'
        db.add_column('ambulancia_responsable', 'dni',
                      self.gf('django.db.models.fields.CharField')(default='A', max_length=10),
                      keep_default=False)

        # Adding field 'Responsable.tipo_trasporte'
        db.add_column('ambulancia_responsable', 'tipo_trasporte',
                      self.gf('django.db.models.fields.CharField')(default='A', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Responsable.dni'
        db.delete_column('ambulancia_responsable', 'dni')

        # Deleting field 'Responsable.tipo_trasporte'
        db.delete_column('ambulancia_responsable', 'tipo_trasporte')


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
            'precio_ambulancia_dia': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'precio_ambulancia_dia_silla': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'precio_km': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'})
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
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ambulancia.Responsable']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'telefono': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'tipo_viaje': ('django.db.models.fields.CharField', [], {'default': "'AS'", 'max_length': '10'})
        },
        'ambulancia.responsable': {
            'Meta': {'object_name': 'Responsable'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo_trasporte': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'})
        }
    }

    complete_apps = ['ambulancia']
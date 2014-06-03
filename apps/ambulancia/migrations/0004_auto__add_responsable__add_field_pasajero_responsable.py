# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Responsable'
        db.create_table('ambulancia_responsable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('ambulancia', ['Responsable'])

        # Adding field 'Pasajero.responsable'
        db.add_column('ambulancia_pasajero', 'responsable',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, default=1, to=orm['ambulancia.Responsable']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Responsable'
        db.delete_table('ambulancia_responsable')

        # Deleting field 'Pasajero.responsable'
        db.delete_column('ambulancia_pasajero', 'responsable_id')


    models = {
        'ambulancia.establecimiento': {
            'Meta': {'object_name': 'Establecimiento'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hora_entrada': ('django.db.models.fields.TimeField', [], {}),
            'hora_salida': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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
            'nombre_padre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nro_obra_social': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'obra_social': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ambulancia.ObraSocial']"}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'default': '1', 'to': "orm['ambulancia.Responsable']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'M'"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tipo_viaje': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'AS'"})
        },
        'ambulancia.responsable': {
            'Meta': {'object_name': 'Responsable'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['ambulancia']
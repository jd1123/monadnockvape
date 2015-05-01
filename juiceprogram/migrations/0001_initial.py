# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'juiceprogram_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_num', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('juices_purchased', self.gf('django.db.models.fields.IntegerField')()),
            ('juices_claimed', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=250)),
        ))
        db.send_create_signal(u'juiceprogram', ['Customer'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'juiceprogram_customer')


    models = {
        u'juiceprogram.customer': {
            'Meta': {'object_name': 'Customer'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_num': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'juices_claimed': ('django.db.models.fields.IntegerField', [], {}),
            'juices_purchased': ('django.db.models.fields.IntegerField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['juiceprogram']
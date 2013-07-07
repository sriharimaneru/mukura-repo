# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'InspireDetail'
        db.delete_table('inspire_inspiredetail')

        # Removing M2M table for field categories on 'InspireDetail'
        db.delete_table('inspire_inspiredetail_categories')

        # Removing M2M table for field posts on 'InspireDetail'
        db.delete_table('inspire_inspiredetail_posts')

        # Adding model 'InspireProfile'
        db.create_table('inspire_inspireprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('time_stamp', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('one_liner', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('inspire', ['InspireProfile'])

        # Adding M2M table for field categories on 'InspireProfile'
        db.create_table('inspire_inspireprofile_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inspireprofile', models.ForeignKey(orm['inspire.inspireprofile'], null=False)),
            ('inspirecategory', models.ForeignKey(orm['inspire.inspirecategory'], null=False))
        ))
        db.create_unique('inspire_inspireprofile_categories', ['inspireprofile_id', 'inspirecategory_id'])

        # Adding M2M table for field posts on 'InspireProfile'
        db.create_table('inspire_inspireprofile_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inspireprofile', models.ForeignKey(orm['inspire.inspireprofile'], null=False)),
            ('post', models.ForeignKey(orm['blog.post'], null=False))
        ))
        db.create_unique('inspire_inspireprofile_posts', ['inspireprofile_id', 'post_id'])


    def backwards(self, orm):
        # Adding model 'InspireDetail'
        db.create_table('inspire_inspiredetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('one_liner', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_stamp', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('inspire', ['InspireDetail'])

        # Adding M2M table for field categories on 'InspireDetail'
        db.create_table('inspire_inspiredetail_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inspiredetail', models.ForeignKey(orm['inspire.inspiredetail'], null=False)),
            ('inspirecategory', models.ForeignKey(orm['inspire.inspirecategory'], null=False))
        ))
        db.create_unique('inspire_inspiredetail_categories', ['inspiredetail_id', 'inspirecategory_id'])

        # Adding M2M table for field posts on 'InspireDetail'
        db.create_table('inspire_inspiredetail_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inspiredetail', models.ForeignKey(orm['inspire.inspiredetail'], null=False)),
            ('post', models.ForeignKey(orm['blog.post'], null=False))
        ))
        db.create_unique('inspire_inspiredetail_posts', ['inspiredetail_id', 'post_id'])

        # Deleting model 'InspireProfile'
        db.delete_table('inspire_inspireprofile')

        # Removing M2M table for field categories on 'InspireProfile'
        db.delete_table('inspire_inspireprofile_categories')

        # Removing M2M table for field posts on 'InspireProfile'
        db.delete_table('inspire_inspireprofile_posts')


    models = {
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.PostCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'time_stamp': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'blog.postcategory': {
            'Meta': {'object_name': 'PostCategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'inspire.inspirecategory': {
            'Meta': {'object_name': 'InspireCategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category_type': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'inspire.inspireprofile': {
            'Meta': {'object_name': 'InspireProfile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['inspire.InspireCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'one_liner': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.Post']", 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'time_stamp': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['inspire']
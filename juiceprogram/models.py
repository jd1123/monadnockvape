from django.db import models
from django.contrib import admin

# Create your models here.

class Customer(models.Model):
	id_num = models.IntegerField(unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	juices_purchased = models.IntegerField()
	juices_claimed = models.IntegerField()
	notes = models.TextField(max_length=250)
    
	def __unicode__(self):
		return self.last_name + ',' + self.first_name

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'id_num','juices_purchased', 'juices_claimed']
    search_fields = ['last_name', 'first_name', 'id_num']

def new_customer(first_name, last_name, juices=0, claimed=0, notes=''):
	print "Calling new_customer"
	l = Customer.objects.count()	
	new_id = Customer.objects.all().order_by('id_num')[l-1].id_num+1
	c = Customer.objects.create(first_name=first_name, last_name=last_name, id_num = new_id, juices_purchased=juices, juices_claimed=claimed, notes=notes)
	return c

def default_customer():
	print "Creating default user"
	c = Customer.objects.create(first_name='John', last_name='Doe', id_num=0, juices_purchased=0, juices_claimed=0)
	c.save()



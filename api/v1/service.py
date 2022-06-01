from django.db import connection
from collections import OrderedDict

def dictfetchall(cursor):
	colums = [col[0] for col in cursor.description]
	return[
		dict(zip(colums, row))
		for row in cursor.fetchall()
	]

def dictfetchone(cursor):
 	desc = cursor.description
 	return dict(zip([col[0] for col in desc], cursor.fetchall()))


def list_category(request):
 	if request.GET.get('user'):
 		user = request.GET.get('user')

 	sql = """
 		select * from blogs_category
 	"""
 	with connection.cursor() as cursor:
 		cursor.execute(sql)
 		data = dictfetchall(cursor)
 	return OrderedDict([
 			("items", data)
 		])

def one_category(request):
 	if request.GET.get('user'):
 		user = request.GET.get('user')

 	sql = """
 		select * from blogs_category
 		where id = %s
 	"""
 	with connection.cursor() as cursor:
 		cursor.execute(sql,[pk])
 		data = dictfetchone(cursor)
 	return OrderedDict([
 			("item", data)
 		])

 def list_diseases(request):
 	if request.GET.get('user'):
 		user = request.GET.get('user')

 	sql = """
 		select * from blogs_diseases

 	"""
 	with connection.cursor()as cursor:
 		cursor.execute(sql)
 		data = dictfetchall(cursor)
 	return OrderedDict([
 			('items', data)
 		])

 def one_diseases(request):
 	if request.GET.get('user'):
 		user = request.GET.get('user')

 	sql = """
 		select * from blogs_diseases
 		where id = %s
 	"""
 	with connection.cursor() as cursor:
 		cursor.execute(sql,[pk])
 		data = dictfetchone(cursor)
 	return OrderedDict([
 			("item", data)
 		])

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import CategorySerializers, DiseasesSerializers, DoctorSerializers, NewsSerializers
from .service import list_category, one_category, list_diseases, one_diseases
from blogs.models import Category, Diseases, Doctors, News


class CategoryView(GenericAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializers


	def get_object(self, *args, **kwargs):
		try:
			if "pk" in kwargs and kwargs['pk']:
				category = Category.objects.get(pk = kwargs['pk'])
		except Exception as e:
			raise NotFound('not faund')
		return category


	# def get(self, request, *args, **kwargs):
	# 	queryset = self.get_queryset()
	# 	serializer = CategorySerializers(queryset, many = True)
	# 	return Response(serializer.data,status = status.HTTP_200_OK)
	
	def get(self, request,*args, **kwargs):
		if 'pk' in kwargs and kwargs['pk']:
			result = one_category(request,kwargs['pk'])
		else:
			result = list_category(request)
		print(result)
		return Response(result, status = status.HTTP_200_OK, content_type = 'application/json')

	def post(self, request,*args, **kwargs):
		serializer = self.get_serializer(data = request.data)  
		serializer.is_valid(raise_exception = True)
		data = serializer.save()
		result = one_category(request, pk = data.id)
		return Response(result, status = status.HTTP_200_OK, content_type='application/json')

	def put(self, request, *args, **kwargs):
		data = self.get_object(*args, **kwargs)
		serializer = self.get_serializer(data = request.data, instance = data, partial = True)
		serializer.is_valed(raise_exception = True)
		data = serializer.save()
		result = one_category(request, pk = data.id)
		return Response(result, status = status.HTTP_200_OK, content_type='application/json')

	def delete(self, request,*args, **kwargs):
		data = Category.objects.get(pk = kwargs['pk'])
		data.delete()
		data.self()
		return Response(None, status = status.HTTP_204_NO_CONTENT)


class DiseasesView(GenericAPIView):
	queryset = Diseases.objects.all()
	serializer_class = DiseasesSerializers

	def get(self, request,*args,**kwargs):
		if 'pk' in kwargs and kwargs['pk']:
			result = one_diseases(request,kwargs['pk'])
		else:
			result = list_diseases(request)

		return Response(result, status = status.HTTP_200_OK, content_type = 'application/json')
		
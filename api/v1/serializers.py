from rest_framework import serializers
from blogs.models import Category, Diseases,Doctors,News


class CategorySerializers(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class  DiseasesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Diseases
		fields = '__all__'

class DoctorSerializers(serializers.ModelSerializer):
	class Meta:
		model = Doctors
		fields = '__all__'

class NewsSerializers(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = '__all__'

	
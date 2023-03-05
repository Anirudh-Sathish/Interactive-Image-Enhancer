from rest_framework import serializers 
from .models import Course 

class CourseSerializer(serializers.modelSerializer):
	class Meta:
		model = course 
		fields = ('name','language','price')

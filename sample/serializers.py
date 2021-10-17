from rest_framework import serializers
from sample.models import *
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=AjaxUdetails
        fields=('id','name','contact','place')
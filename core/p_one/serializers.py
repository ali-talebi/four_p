from rest_framework import serializers 
from .models import p1_methods,avamel,amel_score

class p1_method_serializer(serializers.ModelSerializer):
    class Meta:
        model = p1_methods
        fields = "__all__"




class avamel_serializer(serializers.ModelSerializer):
    model_head = serializers.StringRelatedField()
    class Meta:
        model = avamel
        fields = "__all__"


class p1_method_with_avamels_serializer(serializers.ModelSerializer):

    # avamels = avamel_serializer(many=True,read_only=True)
    avamels = serializers.SerializerMethodField()


    def get_avamels(self,obj):
        return avamel_serializer(obj.avamels.all(),many=True).data

    class Meta:
        model = p1_methods
        fields = "__all__"


class amel_score_serializer(serializers.ModelSerializer):


    class Meta:
        model = amel_score
        fields = "__all__"


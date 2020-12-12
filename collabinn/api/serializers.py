from rest_framework import serializers
from companies.models import CollabRequest

class CollabRequestDataSerializer(serializers.Serializer):
    to_user=serializers.CharField()
    from_user=serializers.CharField()
    
    status = serializers.IntegerField()
    meeting_date=serializers.DateField()
    meeting_location=serializers.CharField()

    def create(self, validated_data):
        return CollabRequest(**validated_data)

    def update(self, instance , validated_data):
        instance.to_user = validated_data.get('to_user',instance.to_user.company_name)
        instance.from_user = validated_data.get('from_user',instance.from_user.company_name)
        instance.status = validated_data.get('status',instance.status)
        instance.meeting_date = validated_data.get('meeting_date',instance.meeting_data)
        instance.meeting_location = validated_data.get('meeting_location',instance.meeting_location)

        instance.save()
        return instance
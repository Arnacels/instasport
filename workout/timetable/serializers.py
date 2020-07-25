from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField
from timetable.models import TimeTableModel

class TimeTableSerializers(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(
            source_field='timetable.TimeTableModel.id'), read_only=True)

    class Meta:
        model = TimeTableModel
        fields = ('id', 'name_workout', 'description', 'date')
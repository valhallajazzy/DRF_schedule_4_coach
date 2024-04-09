from rest_framework import serializers

from schedule_api.models import Client, Coach, SportClub, Training


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'


class SportClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportClub
        fields = '__all__'


class TrainingSerializer(serializers.Serializer):
    training_date = serializers.DateField()
    start_time = serializers.TimeField()
    stop_time = serializers.TimeField()
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    coach = serializers.PrimaryKeyRelatedField(queryset=Coach.objects.all())
    club = serializers.PrimaryKeyRelatedField(queryset=SportClub.objects.all())

    def get_time_intersection(self, database_instance, incoming_instance):
        db_start = database_instance['start_time']
        db_stop = database_instance['stop_time']
        in_start = incoming_instance['start_time']
        in_stop = incoming_instance['stop_time']
        if db_start < in_stop and in_start < db_stop:
            return True
        return False

    def validate(self, data):
        trainings_for_day = Training.objects.filter(
            training_date=data['training_date'],
            coach=data['coach']
        )
        for training in trainings_for_day:
            training_dict = {'start_time': training.start_time, 'stop_time': training.stop_time}
            time_intersection = self.get_time_intersection(training_dict, data)
            if time_intersection is True:
                raise serializers.ValidationError("The entered training time is already occupied")

        return super().validate(data)

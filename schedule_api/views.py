from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from schedule_api.models import Client, Coach, SportClub, Training
from schedule_api.serializers import (ClientSerializer, CoachSerializer,
                                      SportClubSerializer, TrainingSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class CoachViewSet(viewsets.ModelViewSet):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()


class SportClubViewSet(viewsets.ModelViewSet):
    serializer_class = SportClubSerializer
    queryset = SportClub.objects.all()


class TrainingAPIView(APIView):
    def get(self, request):
        trainings = Training.objects.all()
        return Response(TrainingSerializer(trainings, many=True).data)

    def post(self, request):
        serializer = TrainingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_training = Training.objects.create(
            training_date=request.data['training_date'],
            start_time=request.data['start_time'],
            stop_time=request.data['stop_time'],
            client_id=request.data['client'],
            coach_id=request.data['coach'],
            club_id=request.data['club']
        )
        return Response(TrainingSerializer(new_training).data)


class TrainingDestroyAPIView(DestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

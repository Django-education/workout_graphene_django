from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType
from .models import Workout

import graphene


class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout
        fields = "__all__"


class DateWorkoutType(DjangoObjectType):
    class Meta:
        model = Workout
        fields = ("id", "title", "date")


class Query(graphene.ObjectType):
    date_workout = graphene.Field(DateWorkoutType, date=graphene.DateTime())
    id_workout = graphene.Field(WorkoutType, id=graphene.Int())

    def resolve_date_workout(root, info, **kwargs):
        date = kwargs.get('date')
        if date is not None:
            return Workout.objects.get(date=date)
        return None

    def resolve_id_workout(root, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Workout.objects.get(pk=id)
        return None


schema = graphene.Schema(query=Query)

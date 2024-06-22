# schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import health

class healthType(DjangoObjectType):
    class Meta:
        model = health
        fields = ("id", "name", "email", "password", "dob", "contact", "gender", "signupdate",)

class Query(graphene.ObjectType):
    all_patients = graphene.List(healthType)

    def resolve_all_health(root, info):
        return health.objects.all()

schema = graphene.Schema(query=Query)

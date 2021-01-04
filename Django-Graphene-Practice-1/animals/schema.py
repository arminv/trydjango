import graphene
from graphene_django import DjangoObjectType
from .models import Pets, Owners


class AnimalType(DjangoObjectType):
    class Meta:
        model = Pets
        fields = ('id', 'types', 'name', 'owner', 'createdAt', 'img')

class OwnerType(DjangoObjectType):
    class Meta:
        model = Owners
        fields = ('id','username')


class Query(graphene.ObjectType):
    pets = graphene.List(AnimalType)
    owners = graphene.List(OwnerType)

    def resolve_pets(root, info):
        return Pets.objects.all()
        # return Books.objects.filter(title='Book 1')

    def resolve_owners(root, info):
        return Owners.objects.all()


schema = graphene.Schema(query=Query)

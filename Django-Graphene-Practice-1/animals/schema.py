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
        fields = ('id', 'username')


class Query(graphene.ObjectType):
    pets = graphene.List(AnimalType)
    owners = graphene.List(OwnerType)

    def resolve_pets(root, info):
        return Pets.objects.all()
        # return Books.objects.filter(title='Book 1')

    def resolve_owners(root, info):
        return Owners.objects.all()


class AnimalCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        owner = graphene.String(required=True)
        ownerId = graphene.Int(required=False)
        types = graphene.Int(required=True)
        img = graphene.String(required=False)

    animal = graphene.Field(AnimalType)

    @classmethod
    def mutate(cls, root, info, name, owner, ownerId, types, img):
        owner = Owners(id=ownerId, username=owner)
        if owner:
            owner.save()
        else:
            owner = Owners(username=owner)
            owner.save()

        animal = Pets(name=name, owner=owner, types=types, img=img)
        animal.save()
        return AnimalCreateMutation(animal=animal)


class Mutation(graphene.ObjectType):
    create_animal = AnimalCreateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

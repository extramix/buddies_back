import graphene
from graphene_django import DjangoObjectType
from .models import Account, Category, Transaction


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
        fields = "__all__"


class Query(graphene.ObjectType):
    accounts = graphene.List(AccountType)
    categories = graphene.List(CategoryType)
    transactions = graphene.List(TransactionType)

    def resolve_accounts(self, info):
        return Account.objects.all()

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_transactions(self, info):
        return Transaction.objects.all()


schema = graphene.Schema(query=Query)

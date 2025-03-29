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
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("User not authenticated")
        return Account.objects.filter(user=user)

    def resolve_categories(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("User not authenticated")
        return Category.objects.filter(user=user)

    def resolve_transactions(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("User not authenticated")
        return Transaction.objects.filter(account__user=user)


schema = graphene.Schema(query=Query)

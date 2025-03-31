import graphene
from graphene_django import DjangoObjectType
from .models import Account, Category, Transaction
from decimal import Decimal
from graphql import GraphQLError


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class CategorizedType(graphene.ObjectType):
    income = graphene.List(CategoryType)
    expense = graphene.List(CategoryType)

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
        fields = "__all__"


class Query(graphene.ObjectType):
    accounts = graphene.List(AccountType)
    categories = graphene.Field(CategorizedType)
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

        queryset = Category.objects.filter(user=user)
        return {
            "income": queryset.filter(type="INCOME"),
            "expense": queryset.filter(type="EXPENSE"),
        }

    def resolve_transactions(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("User not authenticated")
        return Transaction.objects.filter(account__user=user)


class CreateAccount(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        currency = graphene.String(required=True)

    account = graphene.Field(AccountType)

    def mutate(self, info, name, currency):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("User not authenticated")
        account = Account.objects.create(user=user, name=name, currency=currency)
        return CreateAccount(account=account)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        type = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, type):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("User not authenticated")
        category = Category.objects.create(user=user, name=name, type=type)
        return CreateCategory(category=category)

class CreateTransaction(graphene.Mutation):
    class Arguments:
        account_id = graphene.ID(required=True)
        category_id = graphene.ID(required=True)
        amount = graphene.Float(required=True)
        date = graphene.Date(required=True)
        description = graphene.String(required=True)

    transaction = graphene.Field(TransactionType)

    def mutate(self, info, account_id, category_id, amount, date, description):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("User not authenticated")
        account = Account.objects.get(id=account_id)
        category = Category.objects.get(id=category_id)
        
        if account.user != user:
            raise GraphQLError("You can only create transactions for your own accounts")
        if category.user != user:
            raise GraphQLError("You can only use your own categories")
            
        decimal_amount = Decimal(str(amount))
            
        transaction = Transaction.objects.create(
            account=account,
            category=category,
            amount=decimal_amount,
            date=date,
            description=description
        )
        return CreateTransaction(transaction=transaction)


class Mutation(graphene.ObjectType):
    create_account = CreateAccount.Field()
    create_category = CreateCategory.Field()
    create_transaction = CreateTransaction.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)

from rest_framework import serializers
from .models import Transaction, User, Account, Category


class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    account = serializers.SerializerMethodField()
    
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'category', 'amount', 'date', 'description']

    def get_category(self, obj):
        return {
            'id': obj.category.id,
            'name': obj.category.name,
            'type': obj.category.type
        }

    def get_account(self, obj):
        return {
            'id': obj.account.id,
            'name': obj.account.name,
            'currency': obj.account.currency
        }

    def validate(self, data):
        user = self.context['request'].user
        
        # Validate account ownership
        if data['account'].user != user:
            raise serializers.ValidationError({"account": "You can only create transactions for your own accounts"})
        
        # Validate category ownership
        if data['category'].user != user:
            raise serializers.ValidationError({"category": "You can only use your own categories"})
        
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'currency']
        read_only_fields = ['user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']
        read_only_fields = ['user']

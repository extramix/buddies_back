from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Account, Category, Transaction
from decimal import Decimal
from datetime import date, timedelta

@receiver(post_save, sender=User)
def create_default_data(sender, instance, created, **kwargs):
    if created:
        print(f"Creating default data for new user: {instance.username}")
        default_account = Account.objects.create(
            user=instance,
            name="My JPY Account",
            currency="JPY"
        )
        
        expense_categories = [
            "Food",
            "Transportation",
            "Entertainment",
            "Utilities",
            "Housing",
            "Other"
        ]
        
        expense_category_objects = []
        for name in expense_categories:
            expense_category_objects.append(Category.objects.create(
                user=instance,
                name=name,
                type="EXPENSE"
            ))
        
        income_categories = [
            "Salary",
            "Allowance",
            "Freelance"
        ]
        
        income_category_objects = []
        for name in income_categories:
            income_category_objects.append(Category.objects.create(
                user=instance,
                name=name,
                type="INCOME"
            ))
        
        example_transactions = [
            {
                "account": default_account,
                "category": income_category_objects[0],
                "amount": Decimal("150000.00"),
                "date": date.today() - timedelta(days=28),
                "description": "Monthly salary"
            },
            {
                "account": default_account,
                "category": expense_category_objects[0],
                "amount": Decimal("3500.00"),
                "date": date.today() - timedelta(days=5),
                "description": "Grocery shopping"
            },
            {
                "account": default_account,
                "category": expense_category_objects[1],
                "amount": Decimal("500.00"),
                "date": date.today() - timedelta(days=3),
                "description": "Train fare"
            },
            {
                "account": default_account,
                "category": expense_category_objects[2],
                "amount": Decimal("2000.00"),
                "date": date.today() - timedelta(days=1),
                "description": "Movie tickets"
            },
            {
                "account": default_account,
                "category": income_category_objects[2],
                "amount": Decimal("25000.00"),
                "date": date.today() - timedelta(days=14),
                "description": "Freelance project payment"
            },
            {
                "account": default_account,
                "category": expense_category_objects[3],
                "amount": Decimal("8000.00"),
                "date": date.today() - timedelta(days=10),
                "description": "Electricity bill"
            },
            {
                "account": default_account,
                "category": expense_category_objects[4],
                "amount": Decimal("60000.00"),
                "date": date.today() - timedelta(days=25),
                "description": "Rent payment"
            },
            {
                "account": default_account,
                "category": expense_category_objects[0],
                "amount": Decimal("1500.00"),
                "date": date.today() - timedelta(days=2),
                "description": "Lunch with friends"
            },
            {
                "account": default_account,
                "category": expense_category_objects[5],
                "amount": Decimal("3000.00"),
                "date": date.today() - timedelta(days=7),
                "description": "Medical expenses"
            },
            {
                "account": default_account,
                "category": income_category_objects[1],
                "amount": Decimal("10000.00"),
                "date": date.today() - timedelta(days=20),
                "description": "Monthly allowance"
            },
            {
                "account": default_account,
                "category": expense_category_objects[1],
                "amount": Decimal("1200.00"),
                "date": date.today() - timedelta(days=8),
                "description": "Taxi fare"
            },
            {
                "account": default_account,
                "category": expense_category_objects[2],
                "amount": Decimal("4000.00"),
                "date": date.today() - timedelta(days=12),
                "description": "Concert tickets"
            },
             {
                "account": default_account,
                "category": income_category_objects[3],
                "amount": Decimal("50000.00"),
                "date": date.today() - timedelta(days=22),
                "description": "Stock dividends"
            },
            {
                "account": default_account,
                "category": expense_category_objects[0],
                "amount": Decimal("2200.00"),
                "date": date.today() - timedelta(days=4),
                "description": "Restaurant dinner"
            },
            {
                "account": default_account,
                "category": expense_category_objects[3],
                "amount": Decimal("3500.00"),
                "date": date.today() - timedelta(days=15),
                "description": "Internet bill"
            },
            {
                "account": default_account,
                "category": expense_category_objects[4],
                "amount": Decimal("1500.00"),
                "date": date.today() - timedelta(days=9),
                "description": "Apartment maintenance"
            }
        ]
        
        for tx_data in example_transactions:
            Transaction.objects.create(**tx_data) 
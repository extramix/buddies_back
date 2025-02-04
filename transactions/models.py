from django.db import models
from django.contrib.auth.models import User

TRANSACTION_TYPES = [
    ("INCOME", "Income"),
    ("EXPENSE", "Expense"),
]


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3, default="USD")

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class Category(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name", "type"], name="unique_category"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Transaction(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.account.name} - {self.amount} ({self.date})"

    @property
    def type(self):
        return self.category.type if self.category else None

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
# The Customer model represents users who can place orders.
# Each customer has a name and a unique email.

# The Order model represents purchases made by customers.
# An order is linked to a single customer (one-to-many relationship).
# If a customer is deleted, all their orders are deleted too (on_delete=models.CASCADE).

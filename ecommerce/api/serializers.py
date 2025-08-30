from .models import Product
from rest_framework import serializers
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ["owner", "created_date"]
        #This check if the fields are present i.e (name, price, stock_quantity)
        extra_kwargs = {
            'name' : {"required": True},
            'price' : {"required": True},
            'stock_quantity': {"required": True}
        }

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
      user = User.objects.create_user(
        username = validated_data["username"],
        email = validated_data.get('email'),
        password = validated_data['password']
    )
      return user
        
# Use create_user so password is hashed automatically
    
        # Validate_<fieldname> (self, value):
    # Field validations
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value

#         extra_kwargs = { "field": {"required": True} }

# Only checks that the field is present in the request.

# Example:

# { "name": "Laptop" }


# ⛔ Will fail because "price" and "stock_quantity" are missing.

# ✅ But if you send:

# { "name": "Laptop", "price": -100, "stock_quantity": -5 }


# This will pass — because extra_kwargs doesn’t check values, just existence.

# 🔹 validate_<fieldname>(self, value)

# Checks the value of the field.

# Example:

# def validate_price(self, value):
#     if value <= 0:
#         raise serializers.ValidationError("Price must be greater than 0.")
#     return value


# If you send:

# { "name": "Laptop", "price": -100, "stock_quantity": 5 }


# ⛔ This will fail because -100 is invalid.

# ✅ So…

# extra_kwargs → “Is the field provided at all?”

# validate_<field> → “Is the value acceptable?”

# 👉 Most real projects use both together:

# extra_kwargs for required fields.

# validate_<field> for business rules.
import requests

BASE_URL = 'http://127.0.0.1:5000'

# Add a new product
def add_product(name, description, price):
    response = requests.post(f'{BASE_URL}/products', json={
        'name': name,
        'description': description,
        'price': price
    })
    if response.status_code == 201:
        print("Product added:", response.json())
    else:
        print("Error:", response.json())

# List all products
def list_products():
    response = requests.get(f'{BASE_URL}/products')
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Error:", response.json())

if __name__ == '__main__':
    # Add sample products
    add_product('Laptop', 'A powerful laptop', 1200.50)
    add_product('Mouse', 'Wireless mouse', 25.00)

    # List all products
    list_products()

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory product storage
products = []

# POST /products
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({'error': 'Invalid input'}), 400

    new_product = {
        'id': len(products) + 1,
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(new_product)
    return jsonify(new_product), 201

# GET /products
@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)

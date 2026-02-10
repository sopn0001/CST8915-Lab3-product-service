from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os


def create_app():
    # Load environment variables from a .env file
    load_dotenv()

    app = Flask(__name__)

    # # Enable CORS for all routes and origins
    # CORS(app)


    @app.route('/')
    def hello_world():
        return 'Hello, World! on port 3030'

    from flask_cors import CORS
    @app.route('/products', methods=['GET'])
    def fetch_products():
        products = [{ "id": 1, "name": "Dog Food", "price": 19.99 },
                    { "id": 2, "name": "Cat Food", "price": 34.99 },
                    { "id": 3, "name": "Bird Seeds", "price": 10.99 }]
        return jsonify(products)


    return app

if __name__ == '__main__':
    app = create_app()
    # Get the port from the environment variable or default to 3030
    port = int(os.getenv('PORT', 3030))
    app.run(host='0.0.0.0', port=port)
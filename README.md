# Product Service

The Product Service is a simple web service built using Python and the Flask web framework. It is responsible for serving the product catalog, which includes a list of products that can be fetched via a RESTful API.

## Requirements

- Python 3

## Setup Instructions
1. Navigate to the `product-service` directory:
   ```bash
   cd product-service
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the service:
   ```bash
   python app.py
   ```

The service will be running on http://localhost:3030.

## Testing
1. Install the REST Client extension in VS Code to use .http files.
2. Use the provided test-product-service.http file to test the service.
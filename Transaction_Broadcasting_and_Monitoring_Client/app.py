from transactionClient import TransactionClient
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import requests
import threading
import time

app = Flask(__name__)

client = TransactionClient(
    broadcast_url="https://mock-node-wgqbnxruha-as.a.run.app/broadcast",
    status_url="https://mock-node-wgqbnxruha-as.a.run.app/check"
)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
# Our API url (can of course be a local resource)
API_URL = '/static/swagger.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)


@app.route('/broadcast', methods=['POST'])
def broadcast():
    data = request.json
    symbol = data.get('symbol')
    price = data.get('price')
    timestamp = data.get('timestamp')
    try:
        tx_hash = client.broadcast_transaction(symbol, price, timestamp)
        threading.Thread(target=monitor_transaction, args=(tx_hash,)).start()
        return jsonify({'tx_hash': tx_hash}), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500


@app.route('/status/<tx_hash>', methods=['GET'])
def get_status(tx_hash):
    try:
        status = client.get_transaction_status(tx_hash)
        return jsonify({"tx_status": status})
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


def monitor_transaction(tx_hash):
    status = "PENDING"
    while status not in ['CONFIRMED', 'FAILED']:
        try:
            status = client.get_transaction_status(tx_hash)
            time.sleep(10)
        except requests.RequestException as e:
            print(f"An error occurred while checking status: {e}")
            time.sleep(10)
    print(f"Transaction {tx_hash} status: {status}")


if __name__ == '__main__':
    app.run(debug=True)

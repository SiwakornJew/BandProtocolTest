import requests


class TransactionClient:

    def __init__(self, broadcast_url, status_url):
        self.broadcast_url = broadcast_url
        self.status_url = status_url

    def broadcast_transaction(self, symbol, price, timestamp):
        payload = {
            'symbol': symbol,
            'price': price,
            'timestamp': timestamp
        }
        response = requests.post(self.broadcast_url, json=payload)
        if response.status_code == 200:
            return response.json().get('tx_hash')
        else:
            response.raise_for_status

    def get_transaction_status(self, tx_hash):
        status_url = f"{self.status_url}/{tx_hash}"
        response = requests.get(status_url)
        if response.status_code == 200:
            return response.json().get('tx_status')
        else:
            response.raise_for_status()

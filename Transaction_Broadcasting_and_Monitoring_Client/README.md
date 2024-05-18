
# Transaction Broadcasting and Monitoring Client

Create a client module that is designed to be integrated into another application, with the following capabilities:


## Installation

Install my-project with pip

```bash
  pip install -r requirements.txt

```
## Run project
```bash
 flask -app app run

```
## API Reference

#### POST Broadcast Transaction:

```http
  POST /broadcast
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `symbol` | `string` | **Required**. Transaction symbol, e.g., BTC |
| `price` | `uint64` | **Required**. Symbol price, e.g., 100000 |
| `timestamp` | `uint64` | **Required**. Timestamp of price retrieval |

#### Get status

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `tx_hash`      | `string` | **Required**. The transaction hash |




## Documentation
Swagger
[Documentation](http://127.0.0.1:5000/api/docs)


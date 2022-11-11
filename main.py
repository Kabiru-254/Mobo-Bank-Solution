import ast
import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

data_restPoint = "https://www.npoint.io/docs/26165f9b1c74652ca71d"

parameters = requests.get("https://api.npoint.io/26165f9b1c74652ca71d").json()




@app.route('/')
def home():
    return render_template("index.html", params=parameters)


@app.route('/balance/<transaction_details>')
def invoke(transaction_details):

    transaction_details = ast.literal_eval(transaction_details)
    response = {"transaction_reference": transaction_details["transaction_reference"],
                "transaction_code": transaction_details["transaction_code"],
                "amount": transaction_details["amount"],
                "account_name": "James Bond",
                "phone_number": transaction_details["phone_number"],
                "actual_balance": 500,
                "available_balance": 500
                }
    return render_template("balance.html", transaction_details=response)


if __name__ == "__main__":
    app.run(debug=True)

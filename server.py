import json
import os
import random
from dotenv import load_dotenv
load_dotenv()

from payos import PaymentData, ItemData, PayOS
from flask import Flask, render_template, jsonify, request

PayOS = PayOS(client_id= os.environ.get('PAYOS_CLIENT_ID'),api_key= os.environ.get('PAYOS_API_KEY'), checksum_key= os.environ.get('PAYOS_CHECKSUM_KEY'))

app = Flask(__name__, static_folder='public',
            static_url_path='', template_folder='public')

@app.route('/create_payment_link', methods=['POST'])
def create_payment():
    domain = "http://127.0.0.1:5000"
    try:
       paymentData = PaymentData(
    orderCode=random.randint(1000, 99999),
    amount=99000,
    description="Mở khoá ebook",
    cancelUrl=f"{domain}/cancel.html",
    returnUrl="{https://unlockebookcoaytunguyen.netlify.app/}",
    items=[
        ItemData(
            name="Mở khoá ebook",
            quantity=1,
            price=99000
        )
    ]
)
       payosCreatePayment = PayOS.createPaymentLink(paymentData)
       return jsonify(payosCreatePayment.to_json())
    except Exception as e:
     import traceback
     print(traceback.format_exc())  # In ra lỗi chi tiết trong terminal
     return jsonify(error=str(e)), 403
    
if __name__ == "__main__":
   app.run(port=4242, debug=True)
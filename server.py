import json
import os
import random
import traceback
from dotenv import load_dotenv

from payos import PaymentData, ItemData, PayOS
from flask import Flask, jsonify
from flask_cors import CORS

# Load biến môi trường
load_dotenv()

# Khởi tạo PayOS instance
payos = PayOS(
    client_id=os.environ.get('PAYOS_CLIENT_ID'),
    api_key=os.environ.get('PAYOS_API_KEY'),
    checksum_key=os.environ.get('PAYOS_CHECKSUM_KEY')
)

# Flask app setup
app = Flask(__name__, static_folder='public', static_url_path='', template_folder='public')
CORS(app)

@app.route('/create_payment_link', methods=['POST'])
def create_payment():
    try:
        payment_data = PaymentData(
            orderCode=random.randint(100000, 999999),
            amount=19000,
            description="Đơn hàng ebook",
            cancelUrl="https://canphongrieng2nguoi.io.vn/",  # Khi huỷ
            returnUrl="https://canphongrieng2nguoi.io.vn/success.html",  # Khi thanh toán thành công
            items=[
                ItemData(
                    name="Don hang ebook",
                    quantity=1,
                    price=19000
                )
            ]
        )

        payos_response = payos.createPaymentLink(payment_data)
        return jsonify(payos_response.to_json())

    except Exception as e:
        print("Lỗi khi tạo link thanh toán:")
        print(traceback.format_exc())
        return jsonify(error="Lỗi tạo link thanh toán: " + str(e)), 500

if __name__ == "__main__":
    app.run(port=4242, debug=True)

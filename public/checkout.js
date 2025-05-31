document.getElementById('submit').addEventListener('click', async function () {
  try {
    const response = await fetch('/create_payment_link', {
      method: 'POST'
    });
    const payment = await response.json();

    if (payment.checkoutUrl) {
      window.location.href = payment.checkoutUrl; // iOS cho phép redirect kiểu này
    } else {
      alert("Không lấy được link thanh toán");
    }
  } catch (error) {
    console.error(error);
    alert("Có lỗi xảy ra khi tạo link thanh toán");
  }
});

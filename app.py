import urllib.parse
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Aapka WhatsApp Number
DANCER_WHATSAPP_NUMBER = "918252822382"


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/book", methods=["POST"])
def book_class():
  name = request.form.get("name")
  phone = request.form.get("phone")
  class_type = request.form.get("class_type")
  dance_style = request.form.get("dance_style")
  address = request.form.get("address", "Jamshedpur")

  # WhatsApp message format
  raw_message = (
      f"Hi Rahul! New Dance Class Booking:\n\n"
      f"👤 Name: {name}\n"
      f"📞 Phone: {phone}\n"
      f"🎭 Style: {dance_style}\n"
      f"📍 Class Type: {class_type}\n"
      f"🏠 Address/City: {address}"
  )

  # Encode message for URL
  encoded_message = urllib.parse.quote(raw_message)

  # WhatsApp link redirect
  whatsapp_url = (
      f"https://wa.me/{DANCER_WHATSAPP_NUMBER}?text={encoded_message}"
  )

  return redirect(whatsapp_url)


if __name__ == "__main__":
  app.run(debug=True)
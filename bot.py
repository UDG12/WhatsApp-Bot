from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    if format(msg)=="Hi":
        resp.message("I m Udit's Bot\n You Can contact me Personally on\n 1. Facebook \n 2. Instagram \n 3. LinkedIn")
        return str(resp)
    elif format(msg)=="1":
        resp.message("Facebook - https://www.facebook.com/profile.php?id=100004400377706")
        return str(resp)
    elif format(msg)=="2":
        resp.message("Instagram - https://www.instagram.com/udithacktivist/?hl=en")
        return str(resp)
    elif format(msg)=="3":
        resp.message("LinkedIn - https://www.linkedin.com/in/udit-gupta-943262129/")
        return str(resp)
            

#    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
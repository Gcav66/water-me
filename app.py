from flask import Flask, request, redirect, render_template, send_file
import os
from get_forecast import get_action
import pandas as pd
import twilio.twiml


def create_app():
    app=Flask(__name__)
    return app

app = create_app()

@app.route('/', methods = ['GET','POST'])
def index():
	#action = get_action(5.6, -0.19)
	#df = pd.DataFrame(action)
	#return df.to_html(index=False)
	#message = "FOO"
	body = request.values.get('Body', None)
	message = "Hey, fuck your " + body + " and the horse it rode in on!"
	resp = twilio.twiml.Response()
	resp.message(message)
	return str(resp)

	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=int(port), debug=True)
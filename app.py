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
	body = request.values.get('Body', None)
	mylat = body.split(",")[0]
	mylong = body.split(",")[1]
	try:
		action = get_action(mylat, mylong)
		df = pd.DataFrame(action)
		message = df[['date', 'action']].to_string(index=False)
	except:
		message = "Please provide a single lat/long separated by a comma, e.g., 12.0, -8.0"

	resp = twilio.twiml.Response()
	resp.message(message)
	return str(resp)

	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=int(port), debug=True)
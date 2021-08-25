from imageai.Detection import ObjectDetection
import os
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect, send_from_directory
import requests

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()

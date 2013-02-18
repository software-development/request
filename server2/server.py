import logging
from flask import Flask
from flask import request
from flask import Response
import json

app = Flask("Server 2")
logging.basicConfig(level=logging.DEBUG)

BEACH_PHOTOS = [
  {
    "name": "Cuba",
     "url":"http://farm8.staticflickr.com/7031/6779479599_c8b11ed636_t.jpg"},
  { 
    "name": "Cuba 2",
     "url": "http://farm9.staticflickr.com/8020/7225903096_74e95cbfaf_t.jpg"},
  {
    "name": "Rio",
     "url": "http://farm9.staticflickr.com/8039/8045273721_0a8bac7a2b_t.jpg"},
  {
    "name": "Cayman",
     "url": "http://farm1.staticflickr.com/9/13500136_c32f6092e4_t.jpg"}
]

@app.route("/")
def hello():
  return "Hello from Server 2!"

@app.route("/jsonp")
def get_photos():
  logging.info("---------- Get Photos Endpoint: /jsonp -----------")
  callback = request.args.get('callback', None)
  if callback:
    logging.info("JSON-P Callback is: %s" % callback)
    javascript = "%s(%s);" % (callback, json.dumps(BEACH_PHOTOS))
    return Response(response=javascript,
                    status=200,
                    mimetype="application/javascript")
  else:
    logging.info("No JSON-P Callback. Returning regular JSON")
    json_data = json.dumps(BEACH_PHOTOS)
    return Response(response=json_data,
                    status=200,
                    mimetype="application/json")

if __name__ == "__main__":
  app.debug = True
  app.run(port=9999)

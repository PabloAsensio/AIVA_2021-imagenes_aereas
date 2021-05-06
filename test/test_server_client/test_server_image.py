from flask import Flask, request, Response
import jsonpickle

import numpy as np
import cv2 as cv

app = Flask(__name__)

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request

    # # convert string of image data to uint8
    buf = np.frombuffer(r.data, np.uint8)

    # drop first 17 bytes and last 5, IMAGE INFO
    to_kill_top = 17 * 8
    to_kill_bot = 5 * 8

    # Make image from bytes
    img_arr = buf[to_kill_top:-to_kill_bot].copy() 
    img = cv.imdecode(img_arr, cv.IMREAD_COLOR)


    # ... TODO ...
    cv.imshow("POSTED", img)
    cv.waitKey()
    
 
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}

    response_pickled  = jsonpickle.encode( response )

    return Response(response=response_pickled, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


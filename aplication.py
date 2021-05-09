import base64
import cgi
import json
import socketserver
from http.server import BaseHTTPRequestHandler

import cv2
import cv2 as cv
import numpy as np
import time

from src.NeuralNetwork import NeuralNetwork
from src.TreeDetector import TreeDetector
from src.TreePainter import TreePainter

# To not reload NN
retinanet = NeuralNetwork("./src/model/model.h5")

class Server(BaseHTTPRequestHandler):
    """ Works like Server HTTP """

    def _set_headers(self):
        """ Write headers of responses """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        """ Precess POSTed data (image)  """
        message = self._extract_msg()

        # Extract the image from the JSON that must come in Base64
        base64_img = message['img']
        jpg_img = base64.b64decode(base64_img)
        image = cv2.imdecode(np.frombuffer(jpg_img,dtype=np.int8),1)

        # ---------------------------- IMAGE PROCESSING ----------------------------

        start = time.time()
        print("\n\n\nStarting Image Processing\n\n\n...".upper())

        coordenates = (None, None)

        tree_detector = TreeDetector(retinanet)
        trees = tree_detector.recognize(image, coordenates) 

        tree_painter = TreePainter()
        canvas = tree_painter.draw(image.copy(), trees)

        print("\n\n\nImage Processing Ended. Total time: {:.2f}\n\n\n".format(time.time() - start).upper() )

        # ---------------------------- SEND RESULT ----------------------------

        # Encoding Result
        result_encoded = cv2.imencode('.png', canvas)
        b64_string = base64.b64encode(result_encoded[1]).decode('utf-8')

        # Finally we write the result in a map to send it
        message['result'] = b64_string
        bytes_message = bytes(json.dumps(message),encoding='UTF-8')

        # Send the processed image
        self._set_headers()
        self.wfile.write(bytes_message)

    def _extract_msg(self):
        # We extract the content-type field from the header they send
        header = self.headers.get('content-type')
        ctype, pdict = cgi.parse_header(header)

        # We check that they send us a JSON
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            raise Exception()

        # We read the JSON and put it in a map
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        return message

if __name__ == "__main__":
    
    server_address = ('', 8000)
    httpd = socketserver.TCPServer(server_address, Server)
    print("\nStarting http on port 8000".upper())
    httpd.serve_forever()

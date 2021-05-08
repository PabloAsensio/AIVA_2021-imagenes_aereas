from http.server import BaseHTTPRequestHandler
import socketserver
import base64
import json
import cv2
import cgi
import numpy as np

class Server(BaseHTTPRequestHandler):
    # Clase que actua como Server HTTP

    def _set_headers(self):
        # Método privado que escribe la cabecera de las respuestas
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        # POST Nos envían datos, hacemos la VA y respondemos
        message = self._extract_msg()

        #Primero extraemos la imagen del JSON que debe venir en Base64
        base64_img = message['img']
        jpg_img = base64.b64decode(base64_img)
        img = cv2.imdecode(np.frombuffer(jpg_img,dtype=np.int8),1)

        # ---------------------------- PROCESAMIENTO DE LA IMAGEN ----------------------------
        result = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

        jpg_img = cv2.imencode('.jpg', result)
        b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')

        # ---------------------------- ENVIO DE RESULTADO ----------------------------
        #Finalmente escribimos el resultado en un mapa para enviarlo
        message['result'] = b64_string
        bytes_message = bytes(json.dumps(message),encoding='UTF-8')

        # Finalmente enviamos la respuesta
        self._set_headers()
        self.wfile.write(bytes_message)

    def _extract_msg(self):
        #Extraemos el campo content-type de la cabecera que envían
        header = self.headers.get('content-type')
        ctype, pdict = cgi.parse_header(header)

        # Comprobamos que nos envían un JSON
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            raise Exception()

        # Leemos el JSON y lo metemos en un mapa
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        return message

if __name__ == "__main__":
    
    server_address = ('', 8000)
    httpd = socketserver.TCPServer(server_address, Server)
    print('Starting httpd on port 8000')
    httpd.serve_forever()

from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import tempfile
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8899)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class HttpGetHandler(BaseHTTPRequestHandler):
    #Обработчик с реализованным методом do_GET.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())

def test():
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(['echo', 'a', 'b'], stdout=tempf)
        proc.wait()
        tempf.seek(0)
        print(tempf.read())

def output(cmd):
    cmd_l = cmd.split()
    output = subprocess.Popen(cmd_l, stdout=subprocess.PIPE).communicate()[0]
    output = output.decode("utf-8")
    return (output)


if __name__ == '__main__':
    try:
        run()
        #HttpGetHandler.do_GET()
        while True:
            output()
            print('!')
            continue
    finally:
        print('bye')







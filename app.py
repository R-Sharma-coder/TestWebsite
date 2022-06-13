import http.server
from http.server import BaseHTTPRequestHandler

PORT = 8008


class SimpleHTTPRequestHandler2(BaseHTTPRequestHandler):
    def do_GET(self):
        self.path = "index.html"
        try:
            # Reading the file
            file_to_open = open(self.path).read()
            print("File opened")
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        #     Adds the new header
        # self.headers.add_header('Content-Type' , 'application/excel;RP_AD_008_รายงานUserในระบบ_20220225.xls')
        key = 'application/excel;RP_AD_008_รายงานUserในระบบ_20220225.xls'
        self.send_header("New Key", "New Value")
        self.send_header('Content-Type' ,key.encode("utf-8") )
        # send response headers
        self.end_headers()
        # send the body of the response
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        # print(self.headers)

    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)
        self.write_response(body)

    def write_response(self, content):
        self.send_response(200, "SuccessFull")
        # Sends the existing header.
        self.send_header('Content-Type', "application/excel;RP_AD_008_รายงานUserในระบบ_20220225.xls")
        self.end_headers()
        self.wfile.write(content)
        # self.headers.add_header("Content-Type",)
        print(content.decode('utf-8'))


Handler = SimpleHTTPRequestHandler2
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()
BIND_HOST = "localhost"
# BIND_HOST = "127.0.0.1"
with http.server.HTTPServer((BIND_HOST, PORT), SimpleHTTPRequestHandler2) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# References : https://appdividend.com/2022/01/29/python-simplehttpserver/#:~:text=No%20module%20named%20SimpleHTTPServer%20error%20is%20ModuleNotFoundError%20in,is%20because%20it%20is%20merged%20with%20http.server%20module.

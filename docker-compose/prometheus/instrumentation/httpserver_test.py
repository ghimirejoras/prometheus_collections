import http.server
from prometheus_client import start_http_server, Counter

REQUESTS = Counter('test_requests_total', 'Total GET Requests for our test server')

class Myhandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Test!!!")

if __name__  == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(("localhost", 5000), Myhandler)
    server.serve_forever()



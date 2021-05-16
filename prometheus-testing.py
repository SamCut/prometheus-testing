from prometheus_client import make_wsgi_app
from wsgiref.simple_server import make_server
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

app = make_wsgi_app()
httpd = make_server('', 8000, app)
httpd.serve_forever()
start_wsgi_server(8000)
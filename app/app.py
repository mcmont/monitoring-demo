"""
An example application that exports some metrics.

Derived from the example at https://github.com/prometheus/client_python
"""

from prometheus_client import start_http_server, Counter, Gauge, Histogram, Summary
import random
import time

HTTP_PORT = 8000


# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('app_request_processing_seconds', 'Time spent processing request')
COUNTER = Counter('app_random_count', 'An example counter')
GAUGE = Gauge('app_share_price_gbp', 'Share price in GBP')
HISTOGRAM = Histogram('app_random_histogram', 'An example histogram')


# Decorate function with Summary metric.
@REQUEST_TIME.time()
def process_request(t):
    """A function that generates some metric data."""

    # Add or remove a quantity from the gauge
    if t >= 0.5:
        # Increment the counter half of the time
        COUNTER.inc(t*10) 
        GAUGE.inc(t)
    else:
        GAUGE.dec(t)

    # Add an observation to the histogram
    HISTOGRAM.observe(random.uniform(0.0, 10.0))

    # Sleep for a fraction of a second so that the request time Summary is populated with data.
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(HTTP_PORT)

    # Initialise the gauge
    GAUGE.set(1000)

    # Generate some requests.
    while True:
        process_request(random.random())
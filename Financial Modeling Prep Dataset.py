from fmp_python.fmp import FMP
import certifi
import json

url = "https://financialmodelingprep.com/stable/search-symbol?query=AAPL&apikey=F4h1wP95SrsrfPZT6M28hUdUxIYYX27q"

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

print(get_jsonparsed_data(url))

from fmp_python.fmp import FMP
import certifi
import json
import pandas as pd

# Stock Symbol Search API
url = "https://financialmodelingprep.com/stable/search-symbol?query=AAPL&apikey=F4h1wP95SrsrfPZT6M28hUdUxIYYX27q"

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

AAPL = get_jsonparsed_data(url)

df = pd.DataFrame(AAPL)

# Exporting Data
df.to_excel('FMP Dataset.xlsx', index = False)
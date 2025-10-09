from fmp_python.fmp import FMP
import certifi
import json
import pandas as pd


# FTSE 100 code array
# Upon runnign the code using this array I was getting several missing outputs 
FTSE_Symbols = [
                # 'RTO', 'IMB', 'BRBY', 'BEZ', 'BATS', 'MTLN', 'SHEL', 'ABF', 'CRDA', 'DGE',
                # 'HLN', 'NG', 'MKS', 'UU', 'PSH', 'GLEN', 'AUTO', 'AHT', 'MNG', 'CCEP', 
                # 'CCH', 'SVT ', 'SMIN', 'IAG', 'LMP', 'ULVR', 'HSX', 'AZN', 'BNZL', 'DPLM', 
                # 'RMV', 'ALW', 'HLMA', 'CTEC', 'PRU', 'INF', 'SGRO', 'III', 'VOD', 'RKT', 
                # 'GAW', 'SDR', 'MRO', 'AV', 'FCIT', 'DCC', 'IHG', 'LSEG', 'RR', 'GSK', 
                # 'SMT', 'SSE', 'TSCO', 'BP', 'NXT', 'CNA', 'EXPN', 'SGE', 'STAN', 'SN', 
                # 'PHNX', 'AAL', 'BKG', 'IMI', 'LGEN', 'ADM', 'WTB', 'HWDN', 'EZJ', 'SBRY', 
                # 'PSN', 'BARC', 'HSBA', 'KGF', 'ANTO', 'CPG', 'BTA', 'STJ', 'HIK', 'RIO', 
                # 'PSON', 'AAF', 'ITRK', 'BTRW', 'ICG', 'LAND', 'WPP', 'BA', 'EDV', 'LLOY', 
                # 'PCT', 'NWG', 'FRES', 'REL', 'WEIR', 'BAB', 'SPX', 'JD', 'MNDI', 'ENT'
                ]

# S&P 500 code array 
# I initially wanted to look at the FTSE 100 but it seems like the FMP API only deals with US traded companies
SP500_Symbols = [
                # "MMM", "AOS", "ABT", "ABBV", "ACN", "ATVI", "ADM", "ADBE", "AAP", "AMD", "AES", "AFL", "A", "APD",
                # "AKAM", "ALK", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR",
                # "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS",
                # "ANTM", "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "AGNC", "BXP", "BKR", "BBWI", "BG", "BF.B", "CHRW",
                # "CA", "COF", "CAH", "CBOE", "KMX", "CCL", "CAT", "CBOE", "CBRE", "CDNS", "CZR", "CF", "CFG", "CHD",
                # "CHRW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CTXS", "CLX",
                # "CME", "CMS", "KO", "COL", "CMCSA", "CMA", "CAG", "CXO", "COP", "ED", "STZ", "CE", "COST", "CTRA", "CCI",
                # "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DXCM", "FANG", "DLR",
                # "DFS", "DISCA", "DISCK", "DG", "DLTR", "D", "DOV", "DOW", "DTE", "DUK", "DD", "DXC", "EMN", "ETN", "EBAY",
                # "ECL", "EIX", "EW", "EA", "EMR", "ETR", "EOG", "EFX", "EQIX", "EQR", "ESS", "EL", "EVRG", "ES", "EXC",
                # "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FB", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FRC", "FISV",
                # "FLT", "FMC", "F", "FTNT", "FTV", "FBHS", "FOXA", "FOX", "BEN", "FCX", "GPS", "GRMN", "IT", "GD", "GE",
                # "GIS", "GM", "GPC", "GILD", "GL", "GLW", "GNRC", "GPN", "GS", "GT", "GWW", "HAL", "HBI", "HOG", "HIG",
                # "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE", "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HPQ", "HSIC",
                # "HUM", "HBAN", "HII", "IEX", "IDXX", "INFO", "ITW", "ILMN", "INCY", "IR", "INTC", "ICE", "IBM", "IP", "IPG",
                # "IFF", "INTU", "ISRG", "IVZ", "IPGP", "IQV", "IRM", "JKHY", "J", "JBHT", "SJM", "JNJ", "JCI", "JPM", "JNPR",
                "KSU", "K", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KHC", "KR", "LHX", "LH", "LRCX", "LW", "LVS", "LDOS",
                "LEN", "LLY", "LNC", "LYV", "LKQ", "LMT", "L", "LOW", "LYB", "MTB", "M", "MAC", "MCD", "MCK", "MDT", "MRK",
                "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MA", "MAA", "MRNA", "MHK", "TAP", "MDLZ", "MPWR", "MNST", "MCO",
                "MS", "MSI", "MSCI", "MYL", "NDAQ", "NOV", "NKTR", "NEE", "NLSN", "NKE", "NI", "NBL", "NSC", "NTRS", "NOC",
                "NLOK", "NCLH", "NRG", "NUE", "NVDA", "NVR", "NXPI", "ORLY", "OXY", "ODFL", "OMC", "OKE", "ORCL", "OTIS",
                "PCAR", "PKG", "PARA", "PH", "PAYX", "PAYC", "PYPL", "PNR", "PBCT", "PPL", "PFG", "PG", "PGR", "PLD", "PRU",
                "PTC", "PEG", "PSA", "PHM", "PVH", "QRVO", "PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG", "REGN",
                "RF", "RSG", "RMD", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SEE",
                "SRE", "NOW", "SHW", "SPG", "SWKS", "SLG", "SNA", "SO", "LUV", "SPG", "SWKS", "SNA", "SO", "LUV", "SWKS",
                "SPG", "SWKS", "SNA", "SO", "LUV", "SWKS", "SNA", "SO", "LUV", "SO", "LUV", "SBUX", "STT", "STE", "SYK",
                "SIVB", "SNA", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TGT", "TEL", "FTI", "TDY", "TFX", "TER", "TSLA",
                "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TWTR", "TYL", "TSN", "UDR", "ULTA",
                "USB", "UAA", "UA", "UNP", "UAL", "UNH", "UPS", "URI", "UHS", "UNM", "VLO", "VAR", "VTR", "VRSN", "VRSK", "VZ",
                "VRTX", "VFC", "VIAC", "V", "VMC", "WRB", "WAB", "WMT", "WAT", "WM", "WEC", "WELL", "WST", "WDC", "WU", "WRK",
                "WY" ,"WHR" ,"WMB" ,"WLTW" ,"WYNN" ,"XEL" ,"XLNX" ,"XOM" ,"XRAY" ,"XYL" ,"YUM" ,"ZBRA" ,"ZBH" ,"ZION" ,"ZTS"
                ]

# Stock Symbol Search API
urls = []

# for company in FTSE_Symbols: 
#     link = "https://financialmodelingprep.com/stable/profile?symbol=" + company + "&apikey=F4h1wP95SrsrfPZT6M28hUdUxIYYX27q"
#     urls.append(link)

# Making code more concise with list comprehension 
urls = ["https://financialmodelingprep.com/stable/profile?symbol=" + company + "&apikey=F4h1wP95SrsrfPZT6M28hUdUxIYYX27q" for company in SP500_Symbols]

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

# Run API on all links to get data
df = []

for url in urls: 
    df.append(pd.DataFrame(get_jsonparsed_data(url)))


# Merging DataFrames 
df = pd.concat(df)

# Exporting Data
df.to_excel('FMP Dataset 2.xlsx', index = False)


 
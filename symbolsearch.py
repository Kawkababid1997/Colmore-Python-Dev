import requests

def symbol_search(company_name,api_key):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company_name}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data


import json
import urllib.request
import graphyte
import logging
import time

logging.getLogger().setLevel(logging.INFO)

GRAPHITE_HOST = 'graphite'
CURRENCIES = ['BTC', 'ETH', 'XRP', 'LTC']
SENDER = graphyte.Sender(GRAPHITE_HOST, prefix='currencies')
BASE_URL='https://min-api.cryptocompare.com/data/pricemulti'

def main():
    request = BASE_URL + f'?fsyms={",".join(CURRENCIES)}&tsyms=USD'
    logging.info("Request: %s", request)
    response = json.loads(urllib.request.urlopen(request).read().decode('utf-8'))
    logging.info('Accepted response: %s', response)
    for currency in CURRENCIES:
        SENDER.send(currency, response[currency]['USD'])


if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            logging.exception("Unhandled exception")
        time.sleep(5)

import  cbpro
import pandas as pd
import  websocket
import json
import time
cc = 'btcusd'
interval = '1m'

socket = f'wss://stream.binance.com:9443/ws/{cc}t@kline_{interval}'
closes = []
def on_message(ws, message):
    json_message = json.loads(message)
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        closes.append(float(close))
        print(closes)

    # if len(closes) > 50:
    #     simple_15 = closes[-15:]
    #     simple_50 = closes[-50:]
    #
    #     average_15 = sum(simple_15)/len(simple_15)
    #     average_50 = sum(simple_50)/len(simple_50)

    if len(closes) > 3:
        simple_15 = closes[-2:]
        simple_50 = closes[-3:]

        average_15 = sum(simple_15)/len(simple_15)
        average_50 = sum(simple_50)/len(simple_50)

        if average_15 > average_50:
            print('buy on close')

        time.sleep(60)
    if len(closes) > 2:
        print('if works')
        time.sleep(60)





def on_close(ws):
    print("### closed ###")


ws = websocket.WebSocketApp(socket, on_message = on_message, on_close = on_close)
ws.run_forever()

# passphrase = '5pkxjz9l1d9'
# public_key = '0fb03df8bf3003fed16b3c2d827e71be'
# secret = 'Ve0HP2cYx6dtOSuQsdTjgCTAJjEDeSzsS9iD7O6s/mVIEn0SMcMQnR9xVPhMOfXwXw7COhQqiUvnek5WNwx4rA=='
#
#
#
# auth_client = cbpro.AuthenticatedClient(public_key,secret,passphrase)
# print(auth_client.buy(price = '10.0', size = '0.1', order_type='limit', product_id = 'ETH-USD'))

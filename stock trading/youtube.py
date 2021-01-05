# from new_tos import td_consumer_key, redirect_url, json_path
from td.client import TDClient
td_consumer_key = "HS7K2SZXYBG2HMOYU6JOMXWAWA2QRASG"
redirect_url = "https://localhost/test"
json_paths = 'C:/Users/Admin/github/Random_Projects/stock trading/td_state.json'

td_account = '490558627'

td_client = TDClient(consumer_id = td_consumer_key, redirect_uri = redirect_url, json_path = json_paths)
td_client.login()

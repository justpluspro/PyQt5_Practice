import requests

response = requests.post(
    'http://172.31.243.250:23232/demo/faces/getPage?dbName=spe_1500000200061351078&pageSize=17&index=1', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    })

print(response.json())

import requests
#parse the JSON output and extract the data you need
import json

base = input("Convert from: ")
to = input("Convert to: ")
amount = float(input("Amount: "))

#connect to URL as if you are opening it in browser
response = requests.get('http://api.exchangeratesapi.io/latest?base=' + base)
#response[200] means succesfully connected
print(type(response))

data = response.text
#get str, means string
print(type(data))
#convert the string to JSON
parsed = json.loads(data)
#get dict, dictonary
print(type(parsed))

date = parsed['date']
print("Date:", date, "\n")
usd_rate = parsed['rates']['USD']

rates = parsed['rates']

for currency, rate in rates.items():
    if currency == to:
        conversion = rate * amount
        print("1", base, "=", currency, rate)
        print(amount, base, "=", currency, conversion)

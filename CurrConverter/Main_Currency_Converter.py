import requests

def convert_curr():
    init_currency = input("Enter the initial currency: ")
    target_currency = input(" Enter the target currency: ")

    while True:
        try:
            amount = float(input('Enter the amount: '))
        except:
            print('The amount must be numeric')
            continue
        if not amount > 0:
            print('The amount must be greater than 0')
            continue
        else:
            break

    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "API-KEY"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code

    if status_code != 200:
        result: response.json()
        print('Error response:  ' + str(result))
        quit()

    result = response.json()
    print('Convertion reslut: ' + str(['result']))

if __name__ == '_main_':
    convert_curr()



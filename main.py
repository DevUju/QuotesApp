import requests

CATEGORY = input("What do you need a quote on? Enter one word. E.g, happiness: ").lower()
API_KEY = "PkGY0P0q4Xt4OceCIAhNEg==y5LhNNiQae3UjxrP"
API_URL = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(CATEGORY)


response = requests.get(API_URL, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    quote = response.text
    if len(quote) == 0:
        quote_info = quote.split(":")
        main_quote_info = quote_info[1].split(".")[0]
        apostrophe = '"'
        author_quote = quote_info[-2].split(",")[0][2:-1]
        print(f"{main_quote_info}.{apostrophe} - By {author_quote}.")
    else:
        print("This keyword does not exist in the API!!! Kindly try again.")
else:
    print("Error:", response.status_code, response.text)

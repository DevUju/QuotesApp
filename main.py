import requests
from quote import Quotes

CATEGORY = input("What do you need a quote on? Enter one word. E.g, happiness: ").lower()

classy = Quotes()

new_quote = True
while new_quote:
    API_KEY = "PkGY0P0q4Xt4OceCIAhNEg==y5LhNNiQae3UjxrP"
    API_URL = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(CATEGORY)
    response = requests.get(API_URL, headers={'X-Api-Key': API_KEY})
    quote = response.text
    try:
        if len(quote) > 0:
            classy.print_quote(quote)
    except IndexError:
        classy.no_quote()
    user_info = input("Do you want to get another quote? Type 'yes' or 'no': ").lower()
    if user_info == "yes":
        CATEGORY = input("What do you need a quote on? Enter one word. E.g, happiness: ").lower()
    else:
        new_quote = False

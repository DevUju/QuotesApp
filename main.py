import requests

api = "PkGY0P0q4Xt4OceCIAhNEg==y5LhNNiQae3UjxrP"
category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': api})
if response.status_code == requests.codes.ok:
    quote = response.text
    quote_info = quote.split(":")
    main_quote_info = quote_info[1].split(".")[0]
    apostrophe = '"'
    author_quote = quote_info[-2].split(",")[0][2:-1]
    print(f"{main_quote_info}.{apostrophe} - By {author_quote}.")
else:
    print("Error:", response.status_code, response.text)

class Quotes:
    def _init_(self):
        pass

    def print_quote(self, quote):
        quote_info = quote.split(":")
        main_quote_info = quote_info[1].split(".")[0].lstrip()
        apostrophe = '"'
        author_quote = quote_info[-2].split(",")[0][2:-1]
        print(f"{main_quote_info}.{apostrophe} - By {author_quote}.")

    def no_quote(self):
        print("This keyword does not exist on the API!!! Kindly try again.")




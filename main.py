# A program that read the url and interprets it for use

url = "https://bytebank.com/exchange?currencyOrig=real"
print(url)

index_question = url.find("?")
url_base = url[:index_question]
print(url_base)

url_parameters = url[index_question + 1:]
print(url_parameters)

parameter_search = "currencyOrig"
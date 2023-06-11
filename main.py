#A program that read the url and interprets it for use

url = "https://bytebank.com/exchange?currencyOrig=real"
print(url)


url_base = url[0:29]
print(url_base)

url_parameters = url[29:47]
print(url_parameters)


import re


class ExtractorURL:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    @staticmethod
    def sanitize_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validate_url(self):
        if not self.url:
            raise ValueError("The url is empty")

        url_pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/exchange")
        match = url_pattern.match(self.url)
        if not match:
            raise ValueError("The url is invalid")

    # Divides the url and returns the base
    def get_url_base(self):
        index_question_mark: int = self.url.find("?")
        url_base = self.url[:index_question_mark]
        return url_base

    # Divides the url and returns the parameters
    def get_url_parameters(self):
        url_parameters = self.url[self.url.find("?") + 1:]
        return url_parameters

    # Returns the value of the parameter given
    def get_parameter_value(self, target_parameter):
        url_parameters = self.get_url_parameters()
        index_parameter = url_parameters.find(target_parameter)
        index_parameter_value = index_parameter + len(target_parameter) + 1
        url_parameters_separator = url_parameters.find("&", index_parameter_value)
        if url_parameters_separator == -1:
            url_parameters_value = url_parameters[index_parameter_value:]
        else:
            url_parameters_value = url_parameters[index_parameter_value:url_parameters_separator]
        return url_parameters_value

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url

    def conversion(self):
        currency_origin = self.get_parameter_value("currencyOrigin")
        currency_destination = self.get_parameter_value("currencyDestination")
        amount = float(self.get_parameter_value("amount"))
        if currency_origin == "real" and currency_destination == "dollar":
            conversion_rate = 0.19
        elif currency_origin == "dollar" and currency_destination == "real":
            conversion_rate = 5.30
        else:
            raise ValueError("The currency conversion is not available")

        converted_amount = amount * conversion_rate
        return converted_amount


target_url = ExtractorURL("https://bytebank.com/exchange?currencyDestination=dollar&currencyOrigin=real&amount=1562")
target_url_amount = target_url.get_parameter_value("amount")
target_url_currency_origin = target_url.get_parameter_value("currencyOrigin")
target_url_currency_destination = target_url.get_parameter_value("currencyDestination")

print(target_url_amount)
print(target_url_currency_origin)
print(target_url_currency_destination)
print("The length of the URL is", format(len(target_url)))
print(target_url)
print(target_url.conversion())

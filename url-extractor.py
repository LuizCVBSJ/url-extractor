class ExtractorURL:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validate_url(self):
        if self.url == "":
            raise ValueError("The url is empty")

    def get_url_base(self):
        index_questionMark = self.url.find("?")
        url_base = self.url[:index_questionMark]
        return url_base

    def get_url_parameters(self):
        url_parameters = self.url[self.url.find("?") + 1:]
        return url_parameters

    def get_parameter_value(self, parameter_name):
        url_parameters = self.get_url_parameters()
        index_parameter = url_parameters.find(parameter_search)
        index_parameter_value = index_parameter + len(parameter_search) + 1
        url_parameters_separator = url_parameters.find("&", index_parameter_value)
        if url_parameters_separator == -1:
            url_parameters_value = url_parameters[index_parameter_value:]
        else:
            url_parameters_value = url_parameters[index_parameter_value:url_parameters_separator]
        return url_parameters_value


url = ExtractorURL("https://bytebank.com/exchange?currencyDestination=dolar&currencyOrigin=real&amount=1500")

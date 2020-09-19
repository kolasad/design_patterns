"""
Violates Dependency Inversion Principle
"""


class XMLHttpService:  # low level component
    pass


class Http:  # high level component
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service

    def get(self, url, options):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options):
        self.xml_http_service.request(url, 'POST')


"""
If we want to modify Http to use something else then XML service then we have to change code of Http class
"""


class RESTHttpService:  # low level component
    pass


class Http:  # high level component
    def __init__(self, rest_http_service: RESTHttpService):
        self.xml_http_service = rest_http_service

    def get(self, url, options):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options):
        self.xml_http_service.request(url, 'POST')


"""
How to do it according to Dependency Inversion Principle
"""


class Connection:
    def request(self, url, options):
        raise NotImplementedError


class Http:
    def __init__(self, connection: Connection):
        self.http_connection = connection

    def get(self, url, options):
        self.http_connection.request(url, 'GET')

    def post(self, url, options):
        self.http_connection.request(url, 'POST')


class XMLERequestService(Connection):

    def request(self, url, options):
        pass


"""
Accordingly we can create other Http Connection types
"""


class NodeHttpService(Connection):
    def request(self, url, options):
        pass


class MockHttpService(Connection):
    def request(self, url, options):
        pass

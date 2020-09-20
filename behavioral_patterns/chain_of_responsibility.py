class Authentication:
    def authenticate(self):
        pass


class UserNameAuthentication(Authentication):
    def authenticate(self):
        return False  # we assume that user auth fails


class TokenAuthentication(Authentication):
    def authenticate(self):
        return False  # we assume that token auth fails


class JWTAuthentication(Authentication):
    def authenticate(self):
        return True  # we assume that JWT token auth works


class ChainAuthenticationElement:
    def __init__(self, authentication_handler, next=None):
        self._authentication_handler = authentication_handler
        self._next = next

    def authenticate(self):
        if self._authentication_handler.authenticate():
            print(f'Authentication: {self._authentication_handler.__class__.__name__}')
            return True
        else:
            return self._next and self._next.authenticate()





import threading
import urllib.parse

tls = threading.local()


class BaseTokenSaver:
    def get_token(self, client_id, scopes):
        raise NotImplementedError()

    def add_token(self, client_id, scopes, token):
        raise NotImplementedError()

    def _create_token_hash(self, client_id, scopes):
        assert scopes is not None
        return "%s:%s" % (client_id, ";".join(scopes))


class DefaultTokenSaver(BaseTokenSaver):
    @property
    def storage(self):
        items = getattr(tls, "tokens", None)
        if items is None:
            items = {}
            setattr(tls, "tokens", items)
        return items

    def add_token(self, client_id, scopes, token):
        name = self._create_token_hash(client_id, scopes)
        self.storage[name] = token

    def get_token(self, client_id, scopes):
        name = self._create_token_hash(client_id, scopes)
        return self.storage.get(name)

    @classmethod
    def clear_cache(cls):
        items = getattr(tls, "tokens", {})
        items.clear()


def fix_token_url(token_url: str) -> str:
    """
    Ensure the token url has the right format.

    Often clients only pass the base url instead of the complete
    token url, which gets confusing for users.
    """
    parts = urllib.parse.urlparse(token_url)
    if parts.path == "":
        token_url = urllib.parse.urlunparse((*parts[:2], "/oauth/token", *parts[3:]))
    return token_url

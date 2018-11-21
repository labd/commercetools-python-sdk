import typing

from commercetools import types


class Paginator:
    """This paginator uses the offset kwarg for retrieving the pages"""

    def __init__(self, page_size=20):
        self.page_size = page_size

    def paginate(
        self, operation: typing.Callable, **kwargs: typing.Dict[str, typing.Any]
    ) -> typing.Generator[types.Resource, None, None]:
        if not callable(operation):
            raise ValueError("Expected a callable as first argument")

        if "offset" in kwargs or "limit" in kwargs:
            raise ValueError(
                "It is not possible to supply either the offset or limit "
                "keyword arguments when using the paginator."
            )

        offset = 0
        while True:
            response = operation(**kwargs, offset=offset, limit=self.page_size)
            for item in response.results:
                yield item

            offset += response.count
            if offset >= response.total:
                break

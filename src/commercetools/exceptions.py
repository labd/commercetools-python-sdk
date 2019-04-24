class CommercetoolsError(Exception):
    def __init__(self, message, response, correlation_id=None) -> None:
        super().__init__(message)
        self.response = response
        self.correlation_id = correlation_id

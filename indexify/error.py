class Error(Exception):
    status: str
    message: str

    def __init__(self, status: str, message: str):
        self.status = status
        self.message = message

    @staticmethod
    def parse_error(url: str, error: str) -> "Error":
        status = "GeneralError"
        message = error

        if "extraction_graph" in url:
            status = "ExtractionGraphError"
        elif "search" in url:
            status = "SearchError"

        error = Error(status, message)
        return error

    def __str__(self):
        return f"{self.status} | {self.message.capitalize()}"

    def __repr__(self):
        return f"Error(status={self.status!r}, message={self.message!r})"

from .status import Status

class Response:
  def __init__(
    self,
    status: Status,
    headers: dict
  ) -> None:
    """The Response class is used to make an HTTP response structure

    Args:
      status (Status): This is a status object to define the status code and status text for the response
      headers (dict): This is a dictionary of headers and their values
    """
    self.status = status
    self.headers = headers

  def convertToResponseString(self) -> str:
    """This function converts self into an HTTP response string

    Returns:
      str: The HTTP response string that was generated
    """
    headersAsStrings: str = ""
    for header in self.headers:
      headersAsStrings += f"{header}: {self.headers[header]}\n"
    return f"HTTP/1.1 {self.status.code} {self.status.text}\n{headersAsStrings}\nhello"
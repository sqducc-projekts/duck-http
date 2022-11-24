from .status import Status

class Response:
  def __init__(
    self,
    status: Status,
    headers: dict,
    body: str
  ) -> None:
    """The Response class is used to make an HTTP response structure

    Args:
      status (Status): This is a status object to define the status code and status text for the response
      headers (dict): This is a dictionary of headers and their values
      body (str): This is the response body
    """
    self.status = status
    self.headers = headers
    self.body = body

  def convertToResponseString(self) -> str:
    """This function converts self into an HTTP response string

    Returns:
      str: The HTTP response string that was generated
    """
    headersAsStrings: str = ""
    for header in self.headers:
      headersAsStrings += f"{header}: {self.headers[header]}\n"
    return f"HTTP/1.1 {self.status.code} {self.status.text}\n{headersAsStrings}\n{self.body}"
from .status import Status

__all__ = [
  "Response"
]

class Response:
  def __init__(
    self,
    status: Status,
    body: str,
    headers: dict = {}
  ) -> None:
    """
    The Response class is used to make an HTTP response structure

    Args:
      status (Status): Status class
      body (str): Response body
      headers (dict, optional): Headers. Defaults to {}.
    """
    if type(status) != Status:
      raise TypeError("Status must be of type 'duck_http.Status'")
    else:
      self.status = status
    self.body = str(body)
    if type(headers) != dict:
      raise TypeError("Headers must be of type 'dict'")
    else:
      self.headers = headers

  def __str__(self) -> str:
    """
    HTTP Response string

    Returns:
      str: HTTP Response string so formed
    """
    headerString = ""
    for header in self.headers:
      headerString += str(header) + ": " + str(self.headers[header]) + "\n"
    return "HTTP/1.1 " + str(self.status) + "\n" + headerString + "\n" + str(self.body)

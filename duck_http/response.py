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
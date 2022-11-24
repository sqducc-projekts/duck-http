class Status:
  def __init__(
    self,
    code: int,
    text: str
  ) -> None:
    """The Status class is used for defining the status code and text of a response

    Args:
      code (int): The status code
      text (str): The status text
    """
    self.code = code
    self.text = text
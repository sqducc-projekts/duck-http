__all__ = [
  "Status"
]

class Status:
  def __init__(
    self,
    code: int,
    text: str
  ) -> None:
    """
    This class contains Status code and Status text of a response

    Args:
      code (int): Status code
      text (str): Status text
    """
    self.code = int(code)
    self.text = str(text)

  def __str__(self) -> str:
    """
    HTTP Response Status string

    Returns:
      str: HTTP Response Status string so formed
    """
    return str(self.code) + " " + str(self.text)

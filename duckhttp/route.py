from .examples import hello_world

__all__ = [
  "Route"
]

class Route:
  def __init__(
    self,
    method: str = "GET",
    route: str = "/",
    handler = hello_world
  ) -> None:
    """
    Route class that contains info on a route

    Args:
        method (str, optional): Route method. Defaults to "GET".
        route (str, optional): Route. Defaults to "/".
        handler (Any, optional): A handler that is executed when the route is called. Defaults to 'hello_world' example handler.
    """
    self.method = str(method)
    self.route = str(route)
    self.handler = handler
  
  def __str__(self) -> str:
    """
    Route string

    Returns:
      str: Route string so formed
    """
    return str(self.method) + " " + str(self.route)
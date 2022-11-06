class WikipediaPageNotFoundError(Exception):
    """Exception raised for errors in the wikipedia page name -- title.

    Attributes:
        title -- page title
        message -- explanation of the error
    """

    def __init__(self, title, message=f"Wikipedia page with name {title} not found"):
        self.title = title
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.title} -> {self.message}'


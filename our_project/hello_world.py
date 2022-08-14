class HelloWorld(object):
    """[summary]

    Args:
        object ([type]): [description]
    """

    def __init__(self, hello_text):
        """[summary]

        Args:
            hello_text ([type]): [description]
        """
        super().__init__()
       
        self.hello_text = hello_text
        assert isinstance(self.hello_text, str), f"hello_text must be a string not {type(self.hello_text).__name__}" 

    
    def print_text(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        
        return self.hello_text
        
            
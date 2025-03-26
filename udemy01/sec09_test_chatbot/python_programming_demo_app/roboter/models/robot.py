from roboter.views.console import get_user_input


class Robot:
    def __init__(self, name="Roboko"):
        self.name = name
        self.user_name = ""

    def hello(self):
        self.user_name = get_user_input(
            f"Hello! I am {self.name}. What's your name?")
        print(f"Nice to meet you, {self.user_name}!")

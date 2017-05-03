print("Hello, GitHub!")


class Greeter:

    def __init__(self, message):
        self.message = message

    def greeting(self):
        print(self.message)

greeter = Greeter("Hello from greeter!")
greeter.greeting()

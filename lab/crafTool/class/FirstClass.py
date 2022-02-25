class FirstClass:
    def set_data(self, value):
        self.data = value
    def display(self):
        print(self.data)


x = FirstClass() # Makes a new instance
y = FirstClass() # ---> Each is a new namespace

print('x = {}, y = {}'.format(x, y))

print('===========================')

x.set_data("Repl")


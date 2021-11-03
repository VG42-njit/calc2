number_types = (int, float, complex)


class Calculator:
    def history_static_property(self,x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.validate_args(x, y)
        return x+y

    def multiply(self, x, y):
        self.validate_args(x, y)
        return x*y

    def sub(self, x, y):
        self.validate_args(x, y)
        return x-y

    def div(self, x, y):
        self.validate_args(x, y)
        return x/y


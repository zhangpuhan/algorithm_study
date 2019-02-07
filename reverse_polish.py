class ReversePolish:
    """ this class offers method to evaluate reverse polish equations """
    operations = {
        "+" : (lambda a, b: a + b),
        "-" : (lambda a, b: a - b),
        "*" : (lambda a, b: a * b),
        "/" : (lambda a, b: a / b)
    }

    def evaluate_polish(self, s):
        """ evaluate reverse polish equation using stack """
        stack = []
        string = s.split()

        for char in string:
            if char in self.operations:
                arg_2 = stack.pop()
                arg_1 = stack.pop()
                stack.append(self.operations[char](arg_1, arg_2))
            else:
                stack.append(int(char))

        return stack.pop()         
a = ReversePolish()
print(a.evaluate_polish("990 1 2 + *"))

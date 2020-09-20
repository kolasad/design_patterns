class MathOperationApplier:
    def apply(self, math_operation, first, second):
        if math_operation == '+':
            return first + second
        elif math_operation == '-':
            return first - second
        elif math_operation == '*':
            return first * second
        elif math_operation == '/':
            return first / second


class MathInterpreter(MathOperationApplier):
    def interpret(self, context):
        parsed_context = context.split(' ')
        return self.apply(
            parsed_context[1],
            float(parsed_context[0]),
            float(parsed_context[2])
        )


calculation = input('Podaj działanie (możliwości: (+,-,/,*)) np. 2 + 2: ')
# 2 + 1
# 10 / 150

interpreter = MathInterpreter()
result = interpreter.interpret(calculation)
print(result)


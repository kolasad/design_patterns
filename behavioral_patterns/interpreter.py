class MathOperationApplier:
    def apply(self, math_operation, first, second):
        pass


class MathInterpreter:
    def interpret(self, context):
        pass


calculation = input('Podaj działanie (możliwości: (+,-,/,*)) np. 2+2: ')
# 2+1
# 10/150

interpreter = MathInterpreter()
result = interpreter.interpret(calculation)
print(result)


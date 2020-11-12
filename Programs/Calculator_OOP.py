class Calculator():

    @staticmethod
    def add(a,b):
	    return a+b

    @staticmethod
    def subtract(a, b):
        return a-b

    @staticmethod
    def divide(a, b):
        return a/b

    @staticmethod
    def multiply(a, b):
        return a*b
	
	

calculator = Calculator()
print(calculator.add(5,3))
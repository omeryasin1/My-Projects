class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"

    def store_in_memory(self, value):
        self.memory = value

    def recall_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = 0

def main():
    calc = Calculator()

    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Store in Memory")
        print("6. Recall Memory")
        print("7. Clear Memory")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '8':
            print("Exiting calculator.")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calc.add(num1, num2))
            elif choice == '2':
                print("Result:", calc.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calc.multiply(num1, num2))
            elif choice == '4':
                result = calc.divide(num1, num2)
                print("Result:", result)

        elif choice == '5':
            value = float(input("Enter a value to store in memory: "))
            calc.store_in_memory(value)
            print("Value stored in memory.")

        elif choice == '6':
            print("Recalled value from memory:", calc.recall_memory())

        elif choice == '7':
            calc.clear_memory()
            print("Memory cleared.")

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

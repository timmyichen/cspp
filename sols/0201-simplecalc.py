def solution1(expression):
    operator = expression[1]
    term1 = int(expression[0])
    term2 = int(expression[2])
    
    if operator == "+":
        result = term1 + term2
    elif operator == "-":
        result = term1 - term2
    elif operator == "*":
        result = term1 * term2
    elif operator == "/":
        result = term1 / term2
    elif operator == "%":
        result = term1 % term2
    
    print("The result is {}.".format(result))

def main():
    exp = input("Enter expression: ")
    solution1(exp)
    
if __name__ == "__main__":
    main()
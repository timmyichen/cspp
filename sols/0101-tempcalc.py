def solutionFtoC(temp):
    result = ( float(temp) - 32 ) / 1.8
    print(temp + " F is equal to " + str(result) + " in C")

def solutionCtoF(temp):
    result = float(temp) * 1.8 + 32
    print(temp + " C is equal to " + str(result) + " in F")
    
def main():
    temp = input("Enter temperature in F: ")
    solutionFtoC(temp)
    temp = input("Enter temperature in C: ")
    solutionCtoF(temp)
    
if __name__ == "__main__":
    main()
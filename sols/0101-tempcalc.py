def solutionFtoC(temp):
    result = ( int(temp) - 32 ) / 1.8
    print(temp + " F is equal to " + str(result) + " in C")

def solutionCtoF(temp):
    result = int(temp) * 1.8 + 32
    print(temp + " C is equal to " + str(result) + " in F")
    
def main():
    temp = input("Enter temperature in F: ")
    solutionFtoC(temp)
    temp = input("Enter temperature in C: ")
    solutionCtoF(temp)
    
    
main()
def solution1(sec):
    mins = int(sec / 60) % 60
    hrs = int(sec / 3600)
    sec = sec % 60
    print("{}hr {}m {}s".format(hrs,mins,sec))
    
def solution2(sec):
    mins = sec // 60 % 60
    hrs = sec // 3600
    sec = sec % 60
    print("{}hr {}m {}s".format(hrs,mins,sec))
    
def solution3(sec):
    hrs = sec // 3600
    mins = sec // 60 - (hrs * 60)
    sec = sec % 60
    print("{}hr {}m {}s".format(hrs,mins,sec))

def main():
    sec = input("Enter seconds: ")
    solution3(sec)
    
if __name__ == "__main__":
    main
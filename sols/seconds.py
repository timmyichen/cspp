sec = input("Enter seconds: ")
mins = int(sec / 60) % 60
hrs = int(sec / 3600)
sec = sec % 60
print "{}hr {}m {}s".format(hrs,mins,sec)
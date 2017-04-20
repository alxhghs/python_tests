while True:
    try:
        num = int(input("What number? "))
        print num
        break
    except:
        print "You did not enter a number"

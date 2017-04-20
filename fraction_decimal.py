def calcDecimal():
    while True:
        try:
            numerator = float(raw_input("Enter the numerator: "))
            denominator = float(raw_input("Enter the denominator: "))
            decimal = (numerator / denominator)
            print decimal
        except ValueError:
            print "Program ended."
            break
            
calcDecimal()

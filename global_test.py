a = 47

def global_test():
    global a
    a = 32
    print a
#
# def globe_print():
#     print a

global_test()
# globe_print()

print a

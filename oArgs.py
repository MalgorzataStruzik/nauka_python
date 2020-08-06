#def rzeczy(*args):
#    for arg in args:
#        print(arg)

#rzeczy('krzeslo','kawa','biurko')

def rzeczy(pierwsza_rzecz,*args):
    print(pierwsza_rzecz)
    print(args[0])
    for arg in args:
        print(arg)

rzeczy('lampa','kawa','koc','kloc')

def m2(func):
    def inner(name):

        if name.isalpha():
            print(" valid name")
            func(name)
        else:
            print("not a valid name")
            return

    return inner
@m2
def m1(name):
    print("i am decorated")
if __name__ =='__main__':
    m1()
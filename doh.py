x = []

try:
    print x[0]
    print "not this"
    print x[1]
except IndexError:
    print "doh"

print "you got here"



def check_number(x):
    if x != 7:
        raise Exception("WRONG NUMBER!")


try:
    check_number(6)
except Exception:
    print "sorry, but try again"
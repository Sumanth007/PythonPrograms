def smartDiv(div):
    # print("hi")
    def s(a,b):
        a ,b = max(a,b), min(a,b)
        print("Start")
        div(a,b)
        print("End")
    return s

@smartDiv
def div(a,b):
    print(a/b)

div(100,2000)
#div = smartDiv(div)

# import math as e
# print(e.__name__)
#
# print(e.__doc__)

import math
b = 10
c = print(math.sqrt(b))

def to_title_case(s):
 try:
    return s.title()
 except AttributeError:
    return "Input is not a string"
print(to_title_case(123))
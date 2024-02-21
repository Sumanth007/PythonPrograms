def smartDiv(div):

    def inner(a,b):
        print("Ehll")
        div()
    return inner

@smartDiv
def div():
    print("Hello")

div(10,20)



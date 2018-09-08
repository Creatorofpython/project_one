def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def choicee():
    print("+:ADD")
    print("-:SUB")
    print("*:MUL")
    print("/:DIV")

method={"+":add , "-":sub, "*":mul ,"/":div}
while True:
    choicee()
    select=(input("select your option"))
    if select=='+' or select=="-" or select=="*" or select=="/":
        a=int(input())
        b=int(input())
        method[select](a,b)
    

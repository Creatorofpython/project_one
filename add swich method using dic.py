def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def choicee():
    print("0:ADD")
    print("1:SUB")
    print("2:MUL")
    print("3:DIV")

method={0:add , 1:sub, 2:mul ,3:div}
select=0
while select!=4:
    choicee()
    select=int(input("select your option"))
    if select>=0 and select<4:
        a=int(input())
        b=int(input())
        method[select](a,b)
    
    

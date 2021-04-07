
# class MyClass():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        

#     def My_func(self):
#         print("my age is {} and name is {}".format(self.age,self.name))
# d=MyClass('fazil',25)
# d.My_func()


# #making calculator for grocery store   --!
# def Calculator():
#     sum=0
#     while(True):
#         i=input("enter comodity price or press \'w' to end :" )
#         if i =='w':
#             break

#         else:
#             j=int(input('enter no:'))
#             sum=sum + (int(i) * j )

#     out=input("Do You Want To Make Any Changes ? Press  \'YES OR \'NO :")
#     if out=='YES':
#         sum=0
#         Calculator()
#     elif out=='NO':

#         print(f'total is {sum}')
#     else:
#         print("enter only \'yes or \' no ")
#         Calculator()

# Calculator()



   


# print("the is second line")

            





j=int(input("Press 0 for writing & 1 for rertreiving"))

def take():
    
    
    y=int(input("press 1 for fazil 2 for tuaib 3 for hayan"))
    
    if y==1:
        data=int(input("enter 1 for  exercise or 2  for diet"))
        if data== 1:
            exercise=input("what exercise you did?")
            with open("fazilexercise.txt" ,"a") as fazil:
                fazil.write(exercise)
                print("written succesfully")
        elif data==2:
            diet=input("what diet did you eat?")
            with open("fazildiet.txt" ,"a") as fazil:
                fazil.write(diet)
                print("written succesfully")

    elif y==2:
        data=int(input("enter 1 for  exercise or 2 for diet"))
        if data==1:
            exercise=input("what exercise you did?")
            with open("tuaibexercise.txt" ,"a") as tuaib:
                tuaib.write(exercise)
                print("written succesfully")
        elif data==2:
            diet=input("what diet did you eat?")
            with open("tuaibdiet.txt" ,"a") as tuaib:
                tuaib.write(diet)
                print("written succesfully")

          
    elif y==3:
        data=int(input("enter 1 for  exercise or 2 for diet"))
        if data==1:
            exercise=input("what exercise you did?")
            with open("hayanexercise.txt" ,"a") as hayan:
                hayan.write(exercise)
                print("written succesfully")
        elif data==2:
            diet=input("what diet did you eat?")
            with open("hayandiet.txt" ,"a") as hayan:
                hayan.write(diet)
                print("written succesfully")
        

    
def retreive():
    y=int(input("press 1 for fazil 2 for tuaib 3 for hayan"))
    if y==1:
        data=int(input("enter 1 for exercise and 2 for diet"))
        if data==1:

            with open("fazilexercise.txt" ) as fazil:
                y=fazil.read()
                for i in y:
                    print(i,end="")
        elif data==2:
            with open("fazildiet.txt" ) as fazil:
                y=fazil.read()
                for i in y:
                    print(i,end="")

            
    elif y==2:
        data=int(input("enter 1 for exercise and 2 for diet"))
        if data==1:

            with open("tuaibexercise.txt" ) as tuaib:
                y=tuaib.read()
                for i in y:
                    print(i,end="")
        elif data==2:
            with open("tuaibdiet.txt" ) as tuaib:
                y=tuaib.read()
                for i in y:
                    print(i,end="")

    elif y==3:
        data=int(input("enter 1 for exercise and 2 for diet"))
        if data==1:

            with open("hayanexercise.txt" ) as hayan:
                y=hayan.read()
                for i in y:
                    print(i,end="")
        elif data==2:
            with open("hayandiet.txt" ) as hayan:
                y=hayan.read()
                for i in y:
                    print(i,end="")
        

        
if j==0:
    take()
elif j==1:
    retreive()
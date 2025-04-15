name=input("Enter your name: ")
print("Hello",name)
try:
    num=int(input("Enter a number: "))
    print("You entered",num)
    double_num=2*num
    print("Double the number is",double_num)
except:
    print("Number was not entered")
with open("movies.txt") as file:
    for line in file:
        print(line.strip())
with open("heights.txt") as file:
    for line in file:
       info = line.strip().split()
       info[2]=int(info[2])
       print(info)
file = input("Enter the name of the file: ")
with open(file) as file:
    linenum=1
    for line in file:
        print(line.strip()+" Line number: "+str(linenum))
        linenum+=1
        

#File Handling
#File Open
#File_Close

'''fo = open("1.txt", "w+")
print("Opening file:", fo.name)
print("closed:", fo.closed)
print("opening mode:", fo.mode)
fo.close()
print("closed?:", fo.closed) '''

#file_write

'''fo = open("1.txt", "w")
fo.write("hello world")
fo.close()'''

#file_read

'''fo = open("1.txt", "r+")
str = fo.read(9)
print(str)
str = fo.read()
print(str)
fo.close()'''

#function

'''def printLine(str):
    "function to print line"
    print(str)
    return

printLine('hello')'''

#passbyreference

'''def changeme(mylist):
    "This changes a passsed list into the function"
    mylist.append([1,2,3,4])
    print("values inside the function:", mylist)
    return

    mylist = [10, 20, 30]
    changeme(mylist)
    print("values outside the function:", mylist)'''

#required_argument

'''def fun1(name, age):
    print("Name:", name)
    print("Age:", age)
    return
fun1('Sourabh', 21)'''

#keyword argument

'''def fun1(name, age):
    print("Name:", name)
    print("Age:", age)
    return
fun1(name='sourabh', age=21)'''

#default argument

'''def fun1(name , age=21):
    print("Name is:", name)
    print("Age is:", age)
    return
fun1(age = 22, name = 'sourabh')
fun1('raj')'''

#varibale_length argument

'''def fun1(arg, *vartuple):
    "This prints a variable passsed argument"
    print("Output is:")
    print(arg)
    for var in vartuple:
        print(var)
        return  
    fun1(1)
    fun1(1,2,3,4,5)'''

#anonymous argument

'''mul = lambda arg1, arg2 : arg1 * arg2

print("value of mul:", mul(10, 5))
print("value of multiplication:", mul(5, 5))'''

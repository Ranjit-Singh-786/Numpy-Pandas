import numpy as np
# #             single dimension
# arre = np.array([10,12,11,14,15])    # 1st method
# # arr = np.array([10,12,11,14,15],np.int8) # 2nd method creation and data decleration
# ar = np.arange(1,56).reshape(11,5)    #3 method of declairation array
# ar=np.array(np.arange(1,56).reshape(11,5),dtype=np.int64)    # 4th declairation type with dtype 
# print(ar)
# arr = np.array([10,12,11,14,15],np.int64) # 2nd method creation and data decleration
# print(arre.shape)   #chek how many row and column
# print(arr.dtype)   # for datatype
# arre[1] = 20          #change the value of nmpy array by using index number
# print(arre[1])        #print value by using index
# print("size of element", arre.size)      #chek for size
# print(arre.ndim)
# print("number of byte jitane element he utno ka 4 se multipy kro aswer a jayega",arre.nbytes)
# print(arre.size*4)
# iter = arre.flat
# print(iter)
# for i in iter:
        # print(i)






# arr = np.array(list(range(1,11)))     #array declaration method
# arr = np.array([[i for i in range(1,4)] for j in range(1,4)],np.int16)    #another declairation type of numpy array
# print(arr)
# print(type(arr))
# print(arr.size)
# print(arr.ndim)
# print(arr.shape)
# print(arr.dtype)
# print(arr.ndim)
                                   #slicing method in numpy array

# arr[0] [0] = 15 
# arr[1][1]=30     #particular value change method
# arr[2] [2]= 45          #2 nmvr row update into 16
# print(arr)


# print("no need define the in different bracket you can input your value in single bracket and different bracket as well")
# print()
# arr[0,0] = 15
# arr[1,1]=30
# arr[2,2]=45
# print(arr[0,1])
# print(arr)


# lis1 = list(range(1,20))
# lis2 = list(range(1,20))
# arr2 = np.array([lis1,lis2])
# print(type(arr2))
# print(arr2)


# arr = np.array([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]],np.int32)      
# print(type(arr))
# print(arr)
# arr2 = [[i for i in range(1,4)] for j in range(1,4)]   #numpy array creation using by nested list comprehesion
# arr = np.array(arr2)
# # print("arr2 is printed",arr2)
# print(arr)

# ,,,,,,,,,,,,,,,,,,,,,,,,,double dimension array,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


# arre = np.array([[2,5,1,4,5,1],[5,4,1,2,8,5]],np.int64)   #double dimension
# arre = np.array([[2,5,1,4,5,1],[5,4,1,2,8,5]])
# print("shape = row and column, and size = row*column",arre.size)                                 #chek for size
# print(arre[0,1])                                 #print the value by using index
# print(arre[1,5])                                 #print the value by using index
# print(arre.shape)                                #row and column chek
# print(arre.dtype)
# arre[1,2] = 9  
# arre[0,2] = 9                                 #change the value by using index
# print(arre)
# print()
# print()
# print()

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,zeroes fucntion,,,,,,,,,,,,,,,,,,,,,,


# zone = np.zeros((2,5),np.int32)                      #create a array with filling the zero
# zone = np.zeros((100,100))                               # withaou dtype declairation
# print(type(zone))
# print(zone.size)
# print(zone.dtype)
# print(type(zone))
# d=np.zeros("this is method create for 1d array with zero value:-" ,5,dtype=np.int64)
# print(d)
# print(type(d))
# print(d.dtype)
# print(zone.shape)
# print(zone)
# print()
# print()
# ,,,,,,,,,,,,,,,,,,,,,,,,,,
# func=np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
# print(func)
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,
ar= np.arange(1,25)
print(ar)


# #      arange              create for single dimension array in range
#        reshape             break down a single dimension array into multiple dimension array
#        ravel               is used for convert a multidimension array into single dimension array
# arng = np.arange(1,46)  #declairation or
# here i created a range array 0 to 45 but 45 is not visible so range is 44
# arng = np.arange(48)           #you can assign single in arange function
# print(arng.reshape(6,8)) 
# arng = np.arange(50,101)      #you can also difine a range value like 1 to 100 
# # and here i break these array into 3*15 3 row and 15 column
# # and here i achived the reverese position such a range 
# ab = arng.ravel()                              
# print(ab)
# print(arng.size)
# print(arng.shape)
# print(arng.dtype)
# print(arng)


# #        linspace
# lispac = np.linspace(1,15,12)                       #create similar gapping range array
# lispac = np.linspace(1,10,5)                 # in btwn 2 to 8 create five elment
# print(lispac)
# print(lispac)
# print(lispac.dtype)
# print(lispac.size)
# print(lispac.shape)
# print()
# print()


#  empty
# emp = np.empty((4,6),np.int32)
# print(emp.size) 
        # this method used for create a np array with filling random number
# emp[2,1] = 2
# print(emp)


#    empty_like 
#            used for create a same array according to old array like
#           just like a copy for any array only prototype  copy not a element
# emp_like = np.empty_like(lispac)
# print(lispac)
# print()
# print(emp_like)




#,,,,,,,,,,,,,,,,,,,,, identitiy
#            create for a numnpy array same row size and same column size with filling empty
# ide = np.identity(10)
# ide[1,1] = 2
# print(ide.shape)
# print(ide)
# b = '*'
# for i in ide:
#     print(i=='*')


# ,,,,,,,,,,loop process with flat,,,,,,,,,,

# arr.flat
# for i in arr.flat:
#         print(i)
# ,,,,,,,simply loop process,,,,
# for i in x:
#         for j in i:
#                 print(j)

#,,,,,,,,,,,,,,,using axis,,,,,,,,,,,,,
# {
# axis = 0--> column
# axis = 1--> row
# }


# x = [[1,2,3,],[4,5,6],[7,8,9]]
# arr = np.array(x)
# print(arr)
# print(arr.ndim)

# print(arr)
# print(arr.sum(axis = 0))                      #sum for axis 0 column
# print(arr.sum(axis = 1))                      #sum for axis 1 row
# print(arr.sum())        #add for all elemnt in the numpy array
# print(arr)
# print(arr.max())          #maximum element find in complete array 
# print(arr.min())          #minimum element find in complete array 
# print(type(x))
print(arr.sum())        #total number of sum
print(arr.min())        # minimum element in the array
print(arr.max())         # anyone maximum elment
print(arr.size)



# and now here i m using min and max with axis 
# print(arr)
# b = arr.max(axis = 0) 
# print(b)
# print(arr)
# p = arr.max(axis = 1)
# print(arr.min(axis = 0))
# print(p)


# ,,,,,,,,, # argmax and argmin function in np array used for find the elment min and max
                # but this this function always return a index number of max or min number
                # does not retun the max and min value 
                #    
# print(arr)
# print("this is index value of min element",arr.argmin())
# print("this is index value of max element",arr.argmax())

# ,,,,,,,,,,,,and now argmin and argmax using axis,,,,,,,,,,,,,,,
# print(arr)
# print()
# print(arr.argmax(axis=1))
# print(arr.argmax(axis=0))

# print(arr.argmin(axis=1))
# print(arr.argmin(axis=0))


#,,,,,,,,,,,,,,,,,transpose method for convert row to column.,,,,,,,,,,,,,,
# print(are.transpose())   #if you want sortcut use then u can use only T ok
# print(arr)
# print(arr.T)           #here only capital T used for transpose
# print(arr.ndim)          # used for chek how many dimendsion involved in your array
# print(arr.nbytes)          # chek how many bytes consume in our array
# print(arr.size*4)
# b = arr.flat                  # flat function convert multidimension aray to single dimension
                              # provide the capability of iterator like single dimension
# for i in b:
#     print(i)
               




#            argsort :- sort the array but they only given index 
# print(arr.argsort())        # here argsort using in ndim and again , i will use onle sigle ndim
# array :-[[1 2 3]           #double ndim
# are = np.array([[1,3,4,5],[4,3,5,5],[7,9,3,4]])
# print(are)                                        #here only argsort is suitable 
# print("without paramtr sorting",are.argsort())   #argsort outpt is by default axis 1 sorting and axis 1 is same output to the argsort() 
# q=are.argsort(axis=1)
# d=are.argsort(axis=0)      #out of this method is not suitable 
# print("axis 1 sorting",q)
# print("this is your output")
# print(are)
# print()
# print("axis 0 sorting",d)
#          [4 5 6]
#          [7 8 9]]          ,argsort you can use with axis 
# print(arr)
# output:-[[0 1 2]
#          [0 1 2]
#          [0 1 2]]

#,,,,,,,,,,,,,,,,single dimension argsort,,,,,,,,,,,,

# n = are.ravel()
# n[0] = 9                 # here i used argsort method
# print(n)
# print()
# arr = n. argsort()
# print(arr)



#   argsort with axis
# are[1,0] = 9
# print(are)
# b = are.argsort(axis = 0)
# print(b)
# print(empty_like(are))
# b = are.argsort(axis = 1)
# print(b) 
# d = b.ravel()            #for print the index in linear form]
# cpyary = np.empty_like(d)
# print(cpyary)
# print(type(cpyary))


#<<<<<<<<<< concating of two np array>>>>>>>>>>>>>>>>>>

# arre = np.array([[4,2,3,3],[3,1,5,6],[5,2,8,9]])
#  here i will join two np array
# print(are)
# print()
# print(are)
# print()
# print(are+arre) 




#<<<<<<<<<<<<<<<<<<<<<multiplication>>>>>>>>>>>>>>>>>
# ,,,,,,,,,,if you want to multiply any np array similar vlue to all elment 
# print(are*2)
# print(arr * arre)   #if u wanna mltiply any np ary to any np ary
# print(are)
print()

# print(np.sqrt(are))
# print(arr)
# print()
# print(arr.sum())        #total number of sum
# print(arr.min())        # minimum element in the array
# print(arr.max())         # anyone maximum elment
# print(arr.size)           #total size of element in the aray





# ,,,,,,,,,,myvideo method ,,,,,,,,,,,


# print("flags",are.flags)
# ,,,,,this is output of flags method,,,,,,,,,,,,
# C_CONTIGUOUS : True
#   F_CONTIGUOUS : False
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False
#   UPDATEIFCOPY : False
# print(are)

print()

# print(are.dtype)
# print(are.strides)        #how many bytes consume a single row in aray 
# ,,,,,,strides output,,,,
# (16, 4)
# print(are.transpose())

# ,,,,,,,,,,,,,and now flags and strides using with transpose method,,,,,,,,,,
# d=are.transpose().strides    #here transpose only strides value not a aray transpose
# this is output ---> (4, 16)
# print(d)

# d=are.transpose().flags   #all flags output is printed oposite
# print(d)
import csv
import os
# print(os.getcwd())
os.chdir(r"A:\\pythn\\pandas")
print(os.getcwd())
print(os.listdir())
with open("friend.csv","r") as csv_file:
        csv_reder=csv_file.read()
print(csv_reder)
# print(os.listdir(r"a:\\pythn"))

# open(r"a:\\pythn\\csv_operation.py","x")
# for i in os.listdir(r"a:\\pythn"):
#         if i=="csv_operation.py":
#                 print("this file is exists")
#         else:
#                 print("this file is not your exists")
data = """import csv
import os
print(os.getcwd())
os.chdir(r"A:\\pythn\\pandas")
print(os.getcwd())
print(os.listdir())
with open("friend.csv","r") as csv_file:
        csv_reder=csv_file.read()
print(csv_reder)
print(os.listdir(r"a:\\pythn"))

open(r"a:\\pythn\\csv_operation.py","x")
for i in os.listdir(r"a:\\pythn"):
        if i=="csv_operation.py":
                print("this file is exists")
        else:
                print("this file is not your exists")"""


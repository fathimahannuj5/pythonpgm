# i=11
# while i<=10:
#     print(i)
#     i+=1
# # print("finish")    
# else:
#     print("i is not longer than 10")

# i=1
# while i<=10:
#     if i==4:
#         break
#     print(i)
#     i+=1

i=1
while i<=10:
    i+=1
    if i==4:
        continue
    print(i)
colours=['red','blue','yellow','green']
for i in colours:
    print(i)
# for i in range(10):
#     print(i) 
# for i in range(5,21):
#     print(i)       
# for i in range(4,21,2):
#     print(i) 
# for i in range(3,31,3):
#     print(i) 
# for i in range(3,31):
#     if i%3==0:
#       print(i)        
# list1=[2,4,21,50,26,56,90,45,3]
list1=[2,4,8,9]
for i in list1:
    if i%5==0:
     print(i)
else:
    print("no num divisible by 5")  

# marksinpersentage=[80,90,70,50,65]  
# for i in marksinpersentage:
#     if marks<50:
#         pass
#     else:
#         print("cngrtz")

def addnumbers(a,b):
    sum=a+b
    return sum

result=addnumbers(2,5) 
print(result)  


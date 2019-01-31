# Q1
# lst =[5,4,3,2,1]
# sumlst = sum(lst)
# print (sumlst) 

# Q2
# lst = [1,3,10,30,20,45]
# print (max(lst))

# Q3
# lst = [1,-3,10,30,20,45]
# print (min(lst))

# Q4
# lst = [1,3,10,30,20,45]
# for even in lst:
#     if even % 2 == 0:
#         print(even)

# Q5
# lst = [1,-3,10,30,20,45]
# for num in lst:
#     if num >= 0:
#         print(num)

# Q6
# lst = [1,-3,10,-30,20,45]
# pos= [ ]
# for num in lst:
#      if num > 0:
#         print (num)

# Q7
# lst =[5, 4, 3, 2, 1]
# number= []
# for x in lst:
#     number.append(x * 5)
#     print (number)

 #Q8 
# lst =[5, 4, 3, 2]
# lst1 =[5, 4, 6, 2]
# lst3 = []
# for (x,y) in zip(lst,lst1):
#          z = x*y
#          lst3.append(z)
# print(lst3)
 
#Q9
# lst1 = [ [2, 10], [5, 6] ] 		 
# lst2= [ [1, 8], [10, 3] ]  		 
# result = [ [0, 0], [0, 0] ] 		 
# for x in range(len(lst1)): 
# 	for y in range(len(lst1[0])): 
# 		result[x][y] = lst1[x][y] + lst2[x][y] 
# for r in result: 
# 	print(r) 

# Q10
# lst1 = [ [2, 10], [5, 6] ] 
# lst2= [ [1, 8], [10, 3] ]  
# lst3=[list(map(sum,list(zip(*t)))) for t in zip(lst1,lst2)]
# print (lst3)

# Q11
# a= 1,2,3,4,5,1,3,2,6,1,1,1
# b= 7,8,8,9,6,12
# print (list(set(b+a)))


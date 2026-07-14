#adding elements
b=np.append(x,[6,4,2])
print(b)

#removing elements
print("the elements in X before deleting",x)
newarray=np.delete(x,2)
#elements at index 2 is removed
print("the elements in X after deleting",newarray)

#to modify
b=np.array([6,4,1,3,5,9])
b[b<4]=-1
print(b)

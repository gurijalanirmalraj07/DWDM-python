a=np.array([20,0,40,50])
b=np.arrange(4)
print("the elements in a are",a)
print("the elements in b are",b)
print("result after addition",a+b)
print("result after subtraction",a-b)
print("result after multiplication",a*b)
print("result after division",a/b)

print("result after increasing the number to the power of 4",b**4)
print("result after apllying sin and multiplying with 10",10*np.sin(a))
a[0]+=10
print("result after adding first element with 10",a)
print(np.dot(a,b))

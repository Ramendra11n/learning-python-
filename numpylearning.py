[] 
import numpy as np;
a=np.array([1,2,3,4]);
#  numpy is a library that is extensively used for the manipulations of numeric data and array 
# numpy is considerably fatser than the list and numpy arrays are homogenous(same data type)
print(a);
print(type(a));
print(a.size);
# checking dimension
print(a.ndim);
#  follow zero based indexing
# creating 2-d array 
td=np.array([[1,2,3],[4,5,6]]);
# acccesing the element 
# array_name [row index,column index]
print(td[1,2]);
# reshaping the matrix into 2-d or 3-d array 
a=np.array ([1,2,3,4,5,6]);
j=a.reshape(2,3);
print(j);
k=j.reshape (3,2);#the array itself doesn't suffer from any change it only delivers the array that is the modifeid vlaur of the array.

print(k)
# v.size()
# np.ones(row ,column);
# gives the array whose all values will be ones 
# np.zeroes
# gives the array whose all values will be zeroes
l=np.ones((2,3));
print(l);
o=np.zeros((2,3))
print(o);
# forming the array with the continuous stream 
hj=np.arange(3);# its not the arrange but  a range 
print(hj);
# for forming the matrix with 
same_element=np.full((2,3),8);
print(same_element);
# making an identity matrix
identity=np.eye(3);
print(identity);
# generating the random values in the matrix
rnd=np.random.random((2,3));
print(rnd);
# task 1;
th=np.full((5,5),1);
th[1:4,1:4]=np.zeros((3,3));#you can also update the array while using the slicing it gives the pointer rather than forming the new array.
th[2][2]=9;
print(th);
# np.zeros((3,3));


th[2][2]=9;
list1=[1];
list2=np.zeros((3));
# pyhton always work on the referencing so if you change the second the change wil be reflected in the first  
a=[1,2,3];
b=a;
b[0]=8;
print(a[0]);
# generating duplicates
c=a.copy();
c[0]=1;
print(a[0]);
#  adding the two array element wise  
print(np.add(a,b));
print(np.subtract(a,b));
print(np.multiply(a,b));
print(np.divide(a,b));
# printing the element wise sqrt 
print(np.sqrt(a));
# making the transpose of the matrix
th3=np.array([[1,2,3],[4,5,6]]);
print(th3.T);
# doing complete sum of the array whether 2-d or 3-d
print(np.sum(th3));

#sum function also  takes two arguement the second value tell us the axis across which you want to cokmpute sum of 
print(np.sum(th3,axis=0))
print(np.sum(th3,axis=1))




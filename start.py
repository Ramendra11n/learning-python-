list1=[1,2,3,4,5,6,7,8,9,10];
list2=list1[::-1];
# print(list2);
list3=list1[::2];
#remember when you put the list with the sign -1 then the first element will be treated as the end and second as the beginning
list4=list1[::-2];#==list1
print(list4);
list5=list3+list4;
print(list5);
list6=[1,2];
list7=[2,1];
list7=(list6+list7)*2;
print(list7);
#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def bubbleSort(alist):
    res = ""
    for x in range(len(alist)-1,0,-1):
        for i in range(x):
            if alist[i]>alist[i+1]:
                #print("Swapp", alist[i], alist[i+1])
                res = res + "\nSwapp "+str(alist[i])+" et "+str(alist[i+1])
                temp = alist[i];
                alist[i] = alist[i+1];
                alist[i+1] = temp;
    print(res)
alist = list();
num = int(input("\nEnter number of elements: "));
for i in range(num):
    #n = input("num: ");
    #alist.append(int(n));
    alist.append(num - i)
print("\nThe unsorted array: ");
print(alist);
bubbleSort(alist);
print("\nThe Sorted array: ");
print(alist);
print(chr(42))
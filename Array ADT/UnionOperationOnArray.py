class Array:
    def __init__(self,a,size):
        self.A=a
        self.size=size
        self.length=len(a)
    def display(self):
        for i in self.A:
            print(i,end=" ")
        print()
def Union(arr1,arr2):
    i=j=0
    arr3=[]
    while i<arr1.length and j<arr2.length:
        if arr1.A[i]<arr2.A[j]:
            arr3.append(arr1.A[i])
            i+=1
        elif arr2.A[j]<arr1.A[i]:
            arr3.append(arr2.A[j])
            j+=1
        else:
            arr3.append(arr1.A[i])
            i+=1
            j+=1
    while i<arr1.length:
        arr3.append(arr1.A[i])
        i+=1
    while j<arr2.length:
        arr3.append(arr2.A[j])
        j+=1
    return Array(arr3,20)
arr1=Array([2,3,6,8,10],10)
arr2=Array([1,4,5,8,10],10)
arr3=Union(arr1,arr2)
arr3.display()
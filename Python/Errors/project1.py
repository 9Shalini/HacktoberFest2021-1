

#An array element A[i] is called Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].

def printLeaders(arr,n): 
    for i in range(0,n):
        l=True
        for j in range(i,n):
            if arr[j]>arr[i]:
                l=False
                break
        if l:
            print(arr[i],end=" ")

n=int(input())
arr=[int(x) for x in input().strip().split()]
printLeaders(arr,n)

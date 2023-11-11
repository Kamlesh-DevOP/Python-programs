def binarysearch(L,element):
    start=0
    end=len(L)-1
    if element in L:
        while start<=end:
            mid=(start+end)//2
            if element==L[mid]:
                return mid
            elif element<L[mid]:
                end=mid-1
            else:
                start=mid+1
    else:
        return 'element not found'
print(binarysearch([1,2,3,4,5],2))
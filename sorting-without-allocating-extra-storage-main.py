    
# The SORT() takes an array,A, 
# of integers, an interval indicated by start and end 
# and returns an a new array with the interval in array sorted in ascending order
def SORT(A, start, end):
    for i in range(start - 1, end + 1):
        for j in range(i, end + 1):
            #print(range(i,end+1))
            if A[i] < A[j] or A[i] == A[j]:
                tmp = A[i]
                continue
            else:
                tmp = A[j]
            if tmp == A[i]:
                continue
            else:
                A[j] = A[i]
                A[i] = tmp
    return A
# isEvenSmallest takes an array, A, 
# sorts all its even numbers and places them in front of the array
# while the rest of the odd numbers are placed unsorted at the end 
def isEvenSmallest(A, start, end):
    for i in range(start - 1, end + 1):
        tmp = ''
        for j in range(i, end + 1):
            if A[j] % 2 == 1 :
                continue
            elif tmp == '' and A[j] % 2 == 0:
                tmp = A[j]
                positn = j
                continue
            elif tmp < A[j] or tmp == A[j]:
                continue
            elif tmp > A[j] and A[j] % 2 == 0:
                tmp = A[j]
                positn = j
                continue
        if tmp == A[i]:
            continue
        elif tmp == '':
            continue
        else:
            A[positn] = A[i]
            A[i] = tmp
    return A

# takes an array of integers, 
# reorder its entries so that the even entries appear first.
# without allocating storage.

def sortt(A):
    A = isEvenSmallest(A, 0, len(A) - 1)
    #print(A)
    for i in A:
        if i % 2 == 0:
            continue
        else:
            A = SORT(A, i + 1, len(A) - 1)
            break

    return A

A = [0,1,2,3,4,5,6,7,8,9,9,9,11,12,13,14]
print(sortt(A))



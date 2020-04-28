"""
    The program that's finding pairs in the array.

    The important point is if there are three same number,
it's just 1 pair.


"""
def sockMerchant(n, ar):
    ar.sort()
    pair = 0
    i = 0
    while i < len(ar)-1 :
        if ar[i] == ar[i+1] :
            pair+=1
            i +=2
        else :
            i+=1

    return (pair)





n = int(input())

ar = list(map(int, input().rstrip().split()))

# split() => splits a string. default white space
# rstrip() => removing right spaces
# map(function, iterable)

result = sockMerchant(n, ar)

print (result)

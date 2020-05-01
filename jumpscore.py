"""

input = maximum you can jump 2 index. 0 is safe, 1 is danger. you can't go index of 1.
output = minimum jump score to reach until end.

example inputs:

0 0 1 0 0 1 0

output : 4


"""

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c,n):
    counter = 0
    jump = 0

    while counter < n-1:
        if counter != n-2:
            if c[counter+1] == 1:
                counter+=2
                jump +=1
            else:
                if c[counter+2] == 0:
                    counter +=2
                    jump+=1
                else:
                    counter+=1
                    jump+=1

        else:
            if c[counter+1] == 0:
                counter+=1
                jump +=1
            else:
                break

        
        
        

            
        
    
    return jump
                



n = int(input())

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c,n)

print (result)



'''arr = ['apple', 'sony', 'xiami', 'samsung']
for i in arr:
    print(i, end = ' ')
    if(i == arr[-1]):
        print('\nmother fucker\n')
#print(len(arr))
'''

def fib(n):
    a, b = 0, 1
    arr = []
    while(a <= n):
        arr.append(a)
        #print(a, end = ' ')
        a, b = b, a+b
    print()
    return(arr)

print(fib(2000))




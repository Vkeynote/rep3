##n = int(input())
##print ("Not Weird" if not n%2 and (n in range(2,6) or n>20) else "Weird")
##================================
##n = int(input())
##for i in range(n):
##    print(i*i)
##==================================
##n = int(input())
##print((i*i) for i in range(n))
##===============================
##print(*range(1, int(input())+1), sep='-')


##n = int(input())
##if not n%2 and (n in range(2,6) or n>20):
##    print('Not wierd')
##
##else:
##    print('wierd')

##x = list(input())
##print('-'.join(x)[::-1])

print (input() == 0 or hash(tuple(map(int, input().split(' ')))))

##n = input()
##l = []
##for _ in range(n):
##    s = raw_input().split()
##    cmd = s[0]
##    args = s[1:]
##    if cmd !="print":
##        cmd += "("+ ",".join(args) +")"
##        eval("l."+cmd)
##    else:
##        print (l)


a = 20
b= 10
for i in range(1, 10,1):
    b=b+i
    a=a*i
    print ('a='+str(a))
    print ('b='+str(b))
    b=b+i
    print ('i='+str(i))
print "this is the end"

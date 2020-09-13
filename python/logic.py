import sys

# first
a = 7
b = 14
c = 13
d = 21
ans = 56

# second
a1 = 11
b1 = 26
c1 = 17
d1 = 11
ans1 = 150

# third
a2 = 9
b2 = 32
c2 = 14
d2 = 16



# str="-b*(c+a)+d"
# r=eval(str)
# print(r)

# loops
v =  ['a', 'b', 'c','d']
s1 = [ "", "-", "-(", "("]
s2 = [ "+", "-", "*", "/", ")+", ")-", ")*", ")/", "+(", "-(", "*(", "/(", ")+(", ")-(", ")*(", ")/(" ]
s3 = list( s2)
s4 = list( s2)
s5 = [ "", ")"]

def get_res ( e, a,b,c,d):
    r = eval(e)
    return r


cnt=0
found = False

for i in v:
    #print(i)
    str=i
    for j in v:
        if j != i:
            str=i+j
            for k in v:
                if k!= i and k !=j:
                    str=i+j+k
                    for l in v:
                        if l != k and l !=j and l != i:
                            str = i + j + k+l
                            cnt = cnt+1
                            #print(str)
                            #print (cnt)
                            # brute force operators
                            for o1 in s1:
                                for o2 in s2:
                                    for o3 in s3:
                                        for o4 in s4:
                                            for o5 in s5:
                                                e = o1+i+o2+j+o3+k+o4+l+o5
                                                try:
                                                    r=eval(e)
                                                    found =( r == ans)
                                                except:
                                                    pass
                                                if found:
                                                    print(e + "=", r)
                                                    print("cheking second group")
                                                    r1 = get_res(e,a1,b1,c1,d1)
                                                    found = (r1 == ans1)
                                                    if found:
                                                        print ( "second pass confirmed!")
                                                        print ("Answer:",get_res(e,a2,b2,c2,d2))
                                                        sys.exit(0)
                                                    else:
                                                        print("second pass failed! Keep lookiing..")
if not found:
    print ( "Answer", ans, "not found!" )



# list
l1 = [1,2,3,4,5 ]
print ("l1=", l1)
# boundaries
l2 = l1 [:3]
print ("l1[:3]=", l2)
l3 = l1 [:]
print ("l1[:]=", l3)

# Multi dim
m2 = [[1,2], "qwert",[5,6]]
print (m2)
print (m2[0][0])
print (m2[1][1])

#copy
m3 = list(m2)

#del

del (m2[0])
print (m2)

#append
m2 = m2 + [[8,9]]
print (m2)

# print m3
print (m3)



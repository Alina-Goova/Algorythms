l2=[2, 4, -2, -3, 0 , 11 , 3, -1]
ll=[x if x>0 else l2.index(x) for x in l2]
print(ll)

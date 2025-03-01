j=[]
for i in range (2000,3201):
    j.append(str(i)) if i % 7 == 0 and i % 5 != 0 else None
print(','.join(j))
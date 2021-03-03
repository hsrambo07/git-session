print("hello world")
a=[1,2,3,4,5,2,2,3]
without_dup=[]
for i in a:
    if i not in without_dup:
        without_dup.append(i)
print(without_dup)        

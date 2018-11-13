"""
To find maximum length of duplicated sub-string
"""
a="abscdabscdaresfd"

j=0
i=0
while(i<len(a)):
    if(a.count(a[:i]) == 1):
        j=i
        break
    else:
        i += 1
print(a[:j-1])

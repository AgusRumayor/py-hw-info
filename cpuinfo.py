import sys

data ={}
data['num_processors']=0
for line in sys.stdin:
        lst = line.split(":")
        if len(lst)==2:
                k=lst[0]
                v=lst[1]
                if k == "processor":
                        data['num_processors']+=1
                        data['p_'+str(data['num_processors'])]={}
                data['p_'+str(data['num_processors'])][k]=v
print data
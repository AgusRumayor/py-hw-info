import sys
import redis
import re

r = redis.StrictRedis(host='localhost', port=6379, db=0)
pipe = r.pipeline()
id = pipe.incr('id').get('id').execute()[1]
npr =0
r.set(str(id)+'_'+'num_processors', 0)
pfile = open('/proc/cpuinfo','r')
for line in pfile:
	line = line.replace("\t", "")
        lst = line.split(":")
        if len(lst)==2:
                k=lst[0]
		k=k.replace(" ", "_")
                v=lst[1]
                v=v.rstrip()
                if k == "processor":
                        npr = pipe.incr(str(id)+'_'+'num_processors').get(str(id)+'_'+'num_processors').execute()[1]
                r.hset(str(id)+'_'+'proc_'+str(npr),k,v)

pfile = open('/proc/meminfo','r')
for line in pfile:
        line = line.replace("\t", "")
        lst = line.split(":")
        if len(lst)==2:
                k=lst[0]
                k=k.replace(" ", "_")
                v=lst[1]
                v=v.rstrip()
                r.hset(str(id)+'_'+'mem',k,v)

nst =0
pfile = open('/proc/partitions','r')
for line in pfile:
        lst = line.split()
        if len(lst)==4:
                k=lst[3]
                k=k.replace(" ", "_")
                v=lst[2]
                v=v.rstrip()
		pat = re.search('sd.$', k)
		if pat != None:
                        nst = pipe.incr(str(id)+'_'+'num_storage').get(str(id)+'_'+'num_storage').execute()[1]
                	r.hset(str(id)+'_'+'store',k,v)

pfile = open('/proc/net/dev_mcast','r')
for line in pfile:
        lst = line.split()
        if len(lst)==5:
                k=lst[1]
                k=k.replace(" ", "_")
                v=lst[0]
                v=v.rstrip()
                r.hset(str(id)+'_'+'net',k,v)

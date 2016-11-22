import sys, getopt
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
pipe = r.pipeline()
id = pipe.incr('id').get('id').execute()[1]
npr =0
r.set(str(id)+'_'+'num_processors', 0)
for line in sys.stdin:
        lst = line.split(":")
        if len(lst)==2:
                k=lst[0]
                v=lst[1]
                v=v.rstrip()
                if k == "processor":
                        npr = pipe.incr(str(id)+'_'+'num_processors').get(str(id)+'_'+'num_processors').execute()[1]
                r.hset(str(id)+'_'+'p_'+str(npr),k,v)

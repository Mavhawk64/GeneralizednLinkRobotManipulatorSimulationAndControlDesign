from math import *
from numpy import *
def M(x,N,m):
	s = 0
	for i in range(x,N+1):
		s += m[i-1]
	return s

def delta(p,n,m):
	return M(n,len(m),m) / M(p,len(m),m)

h = 0.1
g = 0.01
t = 0

N = 5

m = []
l = []
tau = []
u = []
for i in range(0,N):
	m.append(1)
	l.append(1)
	tau.append(0)
	u.append(0)
	u.append(0)
o = [u]
f = open("pendulum_output.txt","r").read()
for j in range(0,1000):
	a = []
	for i in range(0,N):
		a.append(u[N+i])
	out = eval(f)
	for i in out:
		a.append(i)
	S = array(a)
	u = u + multiply(S,h)
	o.append(u)
	print(f"{j/1000*100}%")

the_positions = []
for i in range(0,N):
	the_positions.append([])

for x in o:
	for i in range(0,N):
		the_positions[i].append([l[i]*cos(x[i]),l[i]*sin(x[i])])

for i in range(0,N):
	print(the_positions[i])


# for i in range(0,N):
# 	f = open(f"out{i}.txt","w")
# 	f.write(str(the_positions[i]))
# 	f.close()
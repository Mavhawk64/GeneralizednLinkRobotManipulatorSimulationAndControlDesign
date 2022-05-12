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
m = [1,1]
l = [1,1]
tau = [0,0]
u = [0,0,0,0]
o = [u]
for i in range(0,1000):
	S = array([u[2],u[3],(cos(u[0])*g - cos(u[0]-u[1])*cos(u[1])*delta(1,2,m)*g + cos(u[0]-u[1])*delta(1,2,m)*l[0]*sin(u[0]-u[1])*u[2]**2 + cos(u[0]-u[1])*delta(1,2,m)*tau[1]/(M(2,2,m)*l[1]) + delta(1,2,m)*l[1]*sin(u[0]-u[1])*u[3]**2 - tau[0]/(M(1,2,m)*l[0]))/(l[0]*(cos(u[0]-u[1])**2*delta(1,2,m) - 1)),(-cos(u[0]-u[1])*(cos(u[0])*g + delta(1,2,m)*l[1]*sin(u[0]-u[1])*u[3]**2 - tau[0]/(M(1,2,m)*l[0])) + cos(u[1])*g - l[0]*sin(u[0]-u[1])*u[2]**2 - tau[1]/(M(2,2,m)*l[1]))/(l[1]*(cos(u[0]-u[1])**2*delta(1,2,m) - 1))])
	u = u + multiply(S,h)
	o.append(u)

positions1 = []
positions2 = []
for x in o:
	positions1.append([l[0]*cos(x[0]),l[0]*sin(x[0])])
	positions2.append([l[0]*cos(x[1]),l[1]*sin(x[1])])
# print(positions1)
print(positions2)
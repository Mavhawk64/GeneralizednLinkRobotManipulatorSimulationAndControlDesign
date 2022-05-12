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
m = [1,1,1]
l = [1,1,1]
tau = [0,0,0]
u = [0,0,0,0,0,0]
o = [u]
for i in range(0,1000):
	S = array([u[3],u[4],u[5],(-cos(u[0])*cos(u[1]-u[2])**2*delta(2,3,m)*g + cos(u[0])*g - cos(u[0]-u[1])*cos(u[1])*delta(1,2,m)*g + cos(u[0]-u[1])*cos(u[1]-u[2])*cos(u[2])*delta(1,2,m)*delta(2,3,m)*g - cos(u[0]-u[1])*cos(u[1]-u[2])*delta(1,2,m)*delta(2,3,m)*l[0]*sin(u[0]-u[2])*u[3]**2 - cos(u[0]-u[1])*cos(u[1]-u[2])*delta(1,2,m)*delta(2,3,m)*l[1]*sin(u[1]-u[2])*u[4]**2 - cos(u[0]-u[1])*cos(u[1]-u[2])*delta(1,2,m)*delta(2,3,m)*tau[2]/(M(3,3,m)*l[2]) - cos(u[0]-u[1])*delta(1,2,m)*delta(2,3,m)*l[2]*sin(u[1]-u[2])*u[5]**2 + cos(u[0]-u[1])*delta(1,2,m)*l[0]*sin(u[0]-u[1])*u[3]**2 + cos(u[0]-u[1])*delta(1,2,m)*tau[1]/(M(2,3,m)*l[1]) + cos(u[0]-u[2])*cos(u[1])*cos(u[1]-u[2])*delta(1,3,m)*g + cos(u[0]-u[2])*cos(u[1]-u[2])*delta(1,3,m)*delta(2,3,m)*l[2]*sin(u[1]-u[2])*u[5]**2 - cos(u[0]-u[2])*cos(u[1]-u[2])*delta(1,3,m)*l[0]*sin(u[0]-u[1])*u[3]**2 - cos(u[0]-u[2])*cos(u[1]-u[2])*delta(1,3,m)*tau[1]/(M(2,3,m)*l[1]) - cos(u[0]-u[2])*cos(u[2])*delta(1,3,m)*g + cos(u[0]-u[2])*delta(1,3,m)*l[0]*sin(u[0]-u[2])*u[3]**2 + cos(u[0]-u[2])*delta(1,3,m)*l[1]*sin(u[1]-u[2])*u[4]**2 + cos(u[0]-u[2])*delta(1,3,m)*tau[2]/(M(3,3,m)*l[2]) - cos(u[1]-u[2])**2*delta(1,2,m)*delta(2,3,m)*l[1]*sin(u[0]-u[1])*u[4]**2 - cos(u[1]-u[2])**2*delta(1,3,m)*delta(2,3,m)*l[2]*sin(u[0]-u[2])*u[5]**2 + cos(u[1]-u[2])**2*delta(2,3,m)*tau[0]/(M(1,3,m)*l[0]) + delta(1,2,m)*l[1]*sin(u[0]-u[1])*u[4]**2 + delta(1,3,m)*l[2]*sin(u[0]-u[2])*u[5]**2 - tau[0]/(M(1,3,m)*l[0]))/(l[0]*(cos(u[0]-u[1])**2*delta(1,2,m) - cos(u[0]-u[1])*cos(u[0]-u[2])*cos(u[1]-u[2])*delta(1,2,m)*delta(2,3,m) - cos(u[0]-u[1])*cos(u[0]-u[2])*cos(u[1]-u[2])*delta(1,3,m) + cos(u[0]-u[2])**2*delta(1,3,m) + cos(u[1]-u[2])**2*delta(2,3,m) - 1)),(-((cos(u[0]-u[1])**2*delta(1,2,m) - 1)*(cos(u[0]-u[2])**2*delta(1,3,m) - 1) - (cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,2,m) - cos(u[1]-u[2]))*(cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,3,m) - cos(u[1]-u[2])*delta(2,3,m)))*(cos(u[0]-u[1])*(cos(u[0])*g + delta(1,2,m)*l[1]*sin(u[0]-u[1])*u[4]**2 + delta(1,3,m)*l[2]*sin(u[0]-u[2])*u[5]**2 - tau[0]/(M(1,3,m)*l[0])) - cos(u[1])*g - delta(2,3,m)*l[2]*sin(u[1]-u[2])*u[5]**2 + l[0]*sin(u[0]-u[1])*u[3]**2 + tau[1]/(M(2,3,m)*l[1])) + ((cos(u[0]-u[1])**2*delta(1,2,m) - 1)*(cos(u[0]-u[2])*(cos(u[0])*g + delta(1,2,m)*l[1]*sin(u[0]-u[1])*u[4]**2 + delta(1,3,m)*l[2]*sin(u[0]-u[2])*u[5]**2 - tau[0]/(M(1,3,m)*l[0])) - cos(u[2])*g + l[0]*sin(u[0]-u[2])*u[3]**2 + l[1]*sin(u[1]-u[2])*u[4]**2 + tau[2]/(M(3,3,m)*l[2])) - (cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,2,m) - cos(u[1]-u[2]))*(cos(u[0]-u[1])*(cos(u[0])*g + delta(1,2,m)*l[1]*sin(u[0]-u[1])*u[4]**2 + delta(1,3,m)*l[2]*sin(u[0]-u[2])*u[5]**2 - tau[0]/(M(1,3,m)*l[0])) - cos(u[1])*g - delta(2,3,m)*l[2]*sin(u[1]-u[2])*u[5]**2 + l[0]*sin(u[0]-u[1])*u[3]**2 + tau[1]/(M(2,3,m)*l[1])))*(cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,3,m) - cos(u[1]-u[2])*delta(2,3,m)))/(l[1]*(cos(u[0]-u[1])**2*delta(1,2,m) - 1)*((cos(u[0]-u[1])**2*delta(1,2,m) - 1)*(cos(u[0]-u[2])**2*delta(1,3,m) - 1) - (cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,2,m) - cos(u[1]-u[2]))*(cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,3,m) - cos(u[1]-u[2])*delta(2,3,m)))),(-(cos(u[0]-u[1])**2*delta(1,2,m) - 1)*(cos(u[0]-u[2])*(cos(u[0])*g + delta(1,2,m)*l[1]*sin(u[0]-u[1])*u[4]**2 + delta(1,3,m)*l[2]*sin(u[0]-u[2])*u[5]**2 - tau[0]/(M(1,3,m)*l[0])) - cos(u[2])*g + l[0]*sin(u[0]-u[2])*u[3]**2 + l[1]*sin(u[1]-u[2])*u[4]**2 + tau[2]/(M(3,3,m)*l[2])) + (cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,2,m) - cos(u[1]-u[2]))*(cos(u[0]-u[1])*(cos(u[0])*g + delta(1,2,m)*l[1]*sin(u[0]-u[1])*u[4]**2 + delta(1,3,m)*l[2]*sin(u[0]-u[2])*u[5]**2 - tau[0]/(M(1,3,m)*l[0])) - cos(u[1])*g - delta(2,3,m)*l[2]*sin(u[1]-u[2])*u[5]**2 + l[0]*sin(u[0]-u[1])*u[3]**2 + tau[1]/(M(2,3,m)*l[1])))/(l[2]*((cos(u[0]-u[1])**2*delta(1,2,m) - 1)*(cos(u[0]-u[2])**2*delta(1,3,m) - 1) - (cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,2,m) - cos(u[1]-u[2]))*(cos(u[0]-u[1])*cos(u[0]-u[2])*delta(1,3,m) - cos(u[1]-u[2])*delta(2,3,m))))])
	u = u + multiply(S,h)
	o.append(u)

positions1 = []
positions2 = []
positions3 = []
for x in o:
	positions1.append([l[0]*cos(x[0]),l[0]*sin(x[0])])
	positions2.append([l[1]*cos(x[1]),l[1]*sin(x[1])])
	positions3.append([l[2]*cos(x[2]),l[2]*sin(x[2])])
print(positions3)
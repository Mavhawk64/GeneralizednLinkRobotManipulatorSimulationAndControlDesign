from math import *
from numpy import *
import matplotlib.pyplot as plt
def M(x,y,m):
	s = 0
	for i in range(x,y+1):
		s += m[i-1]
	return s

def delta(p,n,m):
	return M(n,len(m),m) / M(p,len(m),m)

def c(p,N,l,m,theta,dottheta):
	cp = 0
	for i in range(p,N):
		n = i + 1
		cp += M(n,N,m) * l[p-1] * l[i] * dottheta[i] ** 2 * sin(theta[p-1] - theta[i])
	for j in range(1,p):
		cp -= M(p,N,m) * l[p-1] * l[j-1] * dottheta[j-1] ** 2 * sin(theta[j-1] - theta[p-1])
	return cp

def G(p,N,l,m,g,theta):
	return M(p,N,m) * l[p-1] * g * cos(theta[p-1])

# This is the element calculation of the M(Theta) matrix.
# x is the column, y is the row
def Mtrx(x,y,N,l,m,theta):
	return M(max(x,y),N,m) * l[x-1] * l[y-1] * cos(theta[min(x-1,y-1)] - theta[max(x-1,y-1)])

def Fatrx(p,N,thetaf,u,KP,KD,KI):
	return KP[p-1] * (thetaf[p-1] - u[N+p-1]) - KD[p-1] * u[2*N+p-1] + KI[p-1] * u[p-1]

# returns c(theta,dottheta), G(theta), and M(theta) as a tuple
def create_matrices(N,l,m,g,u,KP,KD,KI,thetaf):
	# u = [x1,x2,...,xN,t1,t2,...,tN,d1,d2,...,dN] = [u1,u2,...,u3N] -> [u[1-1=0],u[1],...,u[3N-1]]
	x, theta, dottheta = array_split(array(u),3)
	ctrx = []
	gtrx = []
	mtrx = []
	fatrx = []
	for i in range(0,N):
		ctrx.append([c(i+1,N,l,m,theta,dottheta)])
		gtrx.append([G(i+1,N,l,m,g,theta)])
		mtrx.append([])
		fatrx.append([Fatrx(i+1,N,thetaf,u,KP,KD,KI)])
		for j in range(0,N):
			mtrx[i].append(Mtrx(i+1,j+1,N,l,m,theta))
	return ctrx,gtrx,mtrx,fatrx

h = 0.01
t = 0
u = [0,0,0,0,0,0]
g = 0.01
l = [1,1]
m = [1,1]
KP = [10,10]
KD = [10,10]
KI = [10,10]
times = [0]
o = [u]

thetaf = [pi / 2, 0]
for i in range(0,10000):
	ctrx,gtrx,mtrx,fatrx = create_matrices(2,l,m,g,u,KP,KD,KI,thetaf)
	phi = matmul(-linalg.inv(mtrx),array(ctrx) + array(gtrx)) + array(fatrx)
	# print(phi)
	F = matmul(mtrx,fatrx)
	# print(F)
	tau = transpose(F)[0]
	ddt = transpose(phi)[0]
	# print(u[2],u[3])
	H = array([thetaf[0]-u[2],thetaf[1]-u[3],u[4],u[5],ddt[0],ddt[1]])
	u = u + multiply(H,h)
	times.append(h + times[-1])
	o.append(u.tolist())

positions1 = []
positions2 = []
errors1 = []
errors2 = []
for x in o:
	errors1.append(x[0])
	errors2.append(x[1])
	positions1.append([l[0]*cos(x[2]),l[0]*sin(x[2])])
	positions2.append([l[1]*cos(x[3]),l[1]*sin(x[3])])
# print(positions2)

figure = plt.figure()
plt.suptitle(f'Error for {chr(1012)}1')
plt.plot(times,errors1)
# plt.savefig('two_link_err1.png')
plt.show()
plt.suptitle(f'Error for {chr(1012)}2')
plt.plot(times,errors2)
# plt.savefig('two_link_err2.png')
plt.show()
# plt.pause(10)
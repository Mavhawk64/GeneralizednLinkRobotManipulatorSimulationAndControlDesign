from sympy import *
from numpy import *
# from  math import *

# Variable Definitions
N = 2 # 7 gives MemoryError

# \cos(\theta_x-\theta_y) -> co[x*(N+1)+y]
co = []
for i in range(0,N+1):
	for j in range(0,N+1):
		co.append(symbols("co["+str(i*(N+1)+j)+"]"))
# \cos(\theta_x) -> co1[x]
co1 = []
for i in range(0,N+1):
	co1.append(symbols("co1["+str(i)+"]"))
# \delta_{x,y} -> delta_{x~y} -> d[x*(N+1)+y]
d = []
for i in range(0,N+1):
	for j in range(0,N+1):
		d.append(symbols("d["+str(i*(N+1)+j)+"]"))
# \frac{\tau_x}{M_{x,y}l_{x}} -> \frac{\tau_x}{M_{x~y}l_{x}} -> F[x*(N+1)+y]
F = []
for i in range(0,N+1):
	for j in range(0,N+1):
		F.append(symbols("F["+str(i*(N+1)+j)+"]"))
# g -> g
g = symbols('g')
# l_{x} -> l[x]
l = []
for i in range(0,N+1):
	l.append(symbols("l["+str(i)+"]"))
# \sin(\theta_x-\theta_y) -> si[x*(N+1)+y]
si = []
for i in range(0,N+1):
	for j in range(0,N+1):
		si.append(symbols("si["+str(i*(N+1)+j)+"]"))
# \\dot\\theta_x -> v[x]
v = []
for i in range(0,N+1):
	v.append(symbols("v["+str(i)+"]"))


def printMatrix(m):
	ret = ''
	for i in range(0,len(m)):
		ret += '['
		for j in range(0,len(m[i])):
			ret += str(m[i][j]) + ', '
		ret = ret[:-2] + ']\n'
	print(ret)

def printLaTeXMatrix(m):
	ret = "\\begin{bmatrix}\n"
	for i in range(0,len(m)):
		for j in range(0,len(m[i])):
			ret += str(m[i][j]) + " & "
		ret = ret[:-2] + "\\\\\n"
	ret += "\\end{bmatrix}\n"
	print(ret)

def rref(n,m):
	m = ref(n,m)
	i = n-2
	while i >= 0:
		for j in range(1,n-i):
			m[i] = rowSimplify(subtractRowByFactor_s(n,m[i],m[i+j],m[i][i+j]))
		i-=1
	return m

def rref_LaTeX(n,m):
	m = ref_LaTeX(n,m)
	i = n-2
	while i >= 0:
		for j in range(1,n-i):
			m[i] = subtractRowByFactor_LaTeX(n,m[i],m[i+j],m[i][i+j])
		i-=1
	return m

def ref(n,m):
	for i in range(0,n):
		for j in range(0,i):
			m[i] = rowSimplify(subtractRowByFactor_s(n,m[i],m[j],m[i][j]))
		m[i] = rowSimplify(multiplyRowBy_s(n+1,m[i],"1 / (" + m[i][i] + ")"))
	return m

def rowSimplify(r):
	# for c in range(0,len(r)):
		# r[c] = str(eval("simplify("+r[c]+")"))
	return r

def ref_LaTeX(n,m):
	for i in range(0,n):
		for j in range(0,i):
			m[i] = subtractRowByFactor_LaTeX(n,m[i],m[j],m[i][j])
		m[i] = multiplyRowBy_LaTeX(n+1,m[i],"\\frac{1}{" + m[i][i] + "}")
	return m

def multiplyRowBy_s(leng,r,factor):
	for i in range(0,leng):
		r[i] = "(" + r[i] + ")*(" + factor + ")"
	return r

def multiplyRowBy_LaTeX(leng,r,factor):
	for i in range(0,leng):
		r[i] = "\\left(" + r[i] + "\\right)\\cdot\\left(" + factor + "\\right)"
	return r

def subtractRowByFactor_s(n, row, sub, factor):
	cpy = []
	for i in range(0,len(sub)):
		cpy.append(sub[i])
	for i in range(0,n+1):
		row[i] = "(" + row[i] + ")-(" + factor + ")*(" + cpy[i] + ")"
	return row

def subtractRowByFactor_LaTeX(n, row, sub, factor):
	cpy = []
	for i in range(0,len(sub)):
		cpy.append(sub[i])
	for i in range(0,n+1):
		row[i] = "\\left(" + row[i] + "\\right)-\\left(" + factor + "\\right)\\cdot\\left(" + cpy[i] + "\\right)"
	return row

def num_rref(n,m):
	m = num_ref(n,m)
	i = n-2
	while i >= 0:
		for j in range(1,n-i):
			m[i] = subtractRowByFactor(n,m[i],m[i+j],m[i][i+j])
		i-=1
	return m

def num_ref(n,m):
	for i in range(0,n):
		for j in range(0,i):
			m[i] = subtractRowByFactor(n,m[i],m[j],m[i][j])
		m[i] = multiplyRowBy(n+1,m[i],1.0 / m[i][i])
	return m

def multiplyRowBy(leng,r,factor):
	for i in range(0,leng):
		r[i] *= factor
	return r

def subtractRowByFactor(n, row, sub, factor):
	cpy = []
	for i in range(0,len(sub)):
		cpy.append(sub[i])
	for i in range(0,n+1):
		row[i] -= factor * cpy[i]
	return row

def printVectorSol(m):
	ret = ''
	for i in range(0,len(m)):
		ret += '[' + m[i][len(m)] + ']\n'
	print(ret)

def getVectorSol(m):
	c = []
	for i in range(0,len(m)):
		c.append(m[i][len(m)])
	return c

def kinetic_energy(N):
	ret = ""
	for n in range(1,N+1):
		ret += "\\frac{1}{2}\\left("
		for j in range(n,N+1):
			ret += "m_{"+str(j)+"}+"
		ret = ret[:-1] + "\\right)l_{"+str(n)+"}^2\\dot{\\theta}_{"+str(n)+"}^2+"
	for n in range(2,N+1):
		ret += "\\left("
		for j in range(n,N+1):
			ret += "m_{"+str(j)+"}+"
		ret = ret[:-1] + "\\right)\\left("
		for i in range(1,n):
			ret += "l_{"+str(i)+"}l_{"+str(n)+"}\\dot{\\theta}_{"+str(i)+"}\\dot{\\theta}_{"+str(n)+"}\\cos(\\theta_{"+str(i)+"}-\\theta_{"+str(n)+"})+"
		ret = ret[:-1] + "\\right)+"
	ret = ret[:-1]
	return ret

def lag_part_t_theta_p(N,p):
	ret = ""
	if p > 1:
		ret = "\\left("
		for j in range(p,N+1):
			ret += "m_{"+str(j)+"}+"
		ret = ret[:-1] + "\\right)"
	if p > 1:
		ret += "\\left("
	for j in range(1,p):
		ret += "l_{"+str(j)+"}l_{"+str(p)+"}\\dot{\\theta}_{"+str(j)+"}\\dot{\\theta}_{"+str(p)+"}\\sin(\\theta_{"+str(j)+"}-\\theta_{"+str(p)+"})+"
	if p > 1:
		ret = ret[:-1]+"\\right)"
	ret += "-"
	for n in range(p+1,N+1):
		ret += "\\left("
		for j in range(n,N+1):
			ret += "m_{"+str(j)+"}+"
		ret = ret[:-1] + "\\right)l_{"+str(p)+"}l_{"+str(n)+"}\\dot{\\theta}_{"+str(p)+"}\\dot{\\theta}_{"+str(n)+"}\\sin(\\theta_{"+str(p)+"}-\\theta_{"+str(n)+"})-"
	ret = ret[:-1]
	return ret

def mass_sum(bot,top): #inclusive
	ret = "\\left("
	for i in range(bot,top):
		ret += "m_{"+str(i)+"}+"
	ret = ret[:-1] + "\\right)"
	return ret

def lag_part_t_theta_dot_p(N,p):
	ret = mass_sum(p,N+1) + "\\left(l_{"+str(p)+"}^2\\dot{\\theta}_{"+str(p)+"}+"
	for j in range(1,p):
		ret += "l_{"+str(j)+"}l_{"+str(p)+"}\\dot{\\theta}_{"+str(j)+"}\\cos(\\theta_{"+str(j)+"}-\\theta_{"+str(p)+"})+"
	ret = ret[:-1] + "\\right)+"

	for n in range(p+1,N+1):
		ret += mass_sum(n,N+1)+"l_{"+str(n)+"}l_{"+str(p)+"}\\dot{\\theta}_{"+str(n)+"}\\cos(\\theta_{"+str(p)+"}-\\theta_{"+str(n)+"})+"
	ret = ret[:-1]
	return ret

def torque_eq(N,p):
	ret = "l_{"+str(p)+"}\\ddot\\theta_{"+str(p)+"}+"
	for j in range(1,p):
		ret += "l_{"+str(j)+"}\\ddot\\theta_{"+str(j)+"}\\cos(\\theta_{"+str(j)+"}-\\theta_{"+str(p)+"})+"
	for n in range(p+1,N+1):
		ret += "\\delta_{"+str(p)+","+str(n)+"}l_{"+str(n)+"}\\ddot\\theta_{"+str(n)+"}\\cos(\\theta_{"+str(p)+"}-\\theta_{"+str(n)+"})+"
	ret = ret[:-1] + "=" + torque_rhs(N,p)
	return ret

def torque_rhs(N,p):
	ret = "\\frac{\\tau_{"+str(p)+"}}{M_{"+str(p)+","+str(N)+"}l_{"+str(p)+"}}+"
	for j in range(1,p):
		ret += "l_{"+str(j)+"}\\dot\\theta_{"+str(j)+"}^2\\sin(\\theta_{"+str(j)+"}-\\theta_{"+str(p)+"})+"
	ret = ret[:-1] + "-"
	for n in range(p+1,N+1):
		ret += "\\delta_{"+str(p)+","+str(n)+"}l_{"+str(n)+"}\\dot\\theta_{"+str(n)+"}^2\\sin(\\theta_{"+str(p)+"}-\\theta_{"+str(n)+"})-"
	ret += "g\\cos\\theta_{"+str(p)+"}"
	return ret

def torque_sys_eqs(N):
	ret = "\\begin{cases}"
	for i in range(1,N+1):
		ret += torque_eq(N,i) + "\\\\"
	ret += "\\end{cases}"
	return ret

def torque_matrix(N):
	m = []
	# Initialize matrix + set diagonal
	for i in range(0,N):
		m.append([])
		for j in range(0,N+1):
			m[i].append('')
			if i == j:
				m[i][j] = 'l_{'+str(j+1)+'}'
	# Set top section
	for i in range(0,N):
		for j in range(i+1,N):
			m[i][j] = '\\delta_{'+str(i+1)+","+str(j+1)+"}l_{"+str(j+1)+"}\\cos(\\theta_{"+str(i+1)+"}-\\theta_{"+str(j+1)+"})"
	# Set bot section
	for i in range(0, N):
		for j in range(0,i):
			m[i][j] = "l_{"+str(j+1)+"}\\cos(\\theta_{"+str(j+1)+"}-\\theta_{"+str(i+1)+"})"
	# Set RHS section
	for i in range(0,N):
		m[i][N] = torque_rhs(N,i+1)
	return m

def torque_matrix_sym(N):
	m = []
	# Initialize matrix + set diagonal
	for i in range(0,N):
		m.append([])
		for j in range(0,N+1):
			m[i].append('')
			if i == j:
				m[i][j] = 'l['+str(j+1)+']'
	# Set top section
	for i in range(0,N):
		for j in range(i+1,N):
			m[i][j] = 'delta('+str(i+1)+"~"+str(j+1)+"~m)*l["+str(j+1)+"]*cos(u["+str(i+1)+"]-u["+str(j+1)+"])"
	# Set bot section
	for i in range(0, N):
		for j in range(0,i):
			m[i][j] = "l["+str(j+1)+"]*cos(u["+str(j+1)+"]-u["+str(i+1)+"])"
	# Set RHS section
	for i in range(0,N):
		m[i][N] = torque_rhs_sym(N,i+1)
	return m

def torque_rhs_sym(N,p):
	ret = "tau["+str(p)+"]/(M("+str(p)+"~"+str(N)+"~m)*l["+str(p)+"])+"
	for j in range(1,p):
		ret += "l["+str(j)+"]*v["+str(j)+"]**2*sin(u["+str(j)+"]-u["+str(p)+"])+"
	ret = ret[:-1] + "-"
	for n in range(p+1,N+1):
		ret += "delta("+str(p)+"~"+str(n)+"~m)*l["+str(n)+"]*v["+str(n)+"]**2*sin(u["+str(p)+"]-u["+str(n)+"])-"
	ret += "g*cos(u["+str(p)+"])"
	return ret

def set_values_latex():
	# \cos(\theta_x-\theta_y) -> co[x*(N+1)+y]
	co = []
	for i in range(0,N+1):
		for j in range(0,N+1):
			co.append(symbols("\\cos(\\theta_{"+str(i)+"}-\\theta_{"+str(j)+"})"))
	# \cos(\theta_x) -> co1[x]
	co1 = []
	for i in range(0,N+1):
		co1.append(symbols("\\cos(\\theta_{"+str(i)+"})"))
	# \delta_{x,y} -> delta_{x~y} -> d[x*(N+1)+y]
	d = []
	for i in range(0,N+1):
		for j in range(0,N+1):
			d.append(symbols("\\delta_{"+str(i)+"~"+str(j)+"}"))
	# \frac{\tau_x}{M_{x,y}l_{x}} -> \frac{\tau_x}{M_{x~y}l_{x}} -> F[x*(N+1)+y]
	F = []
	for i in range(0,N+1):
		for j in range(0,N+1):
			F.append(symbols("\\frac{\\tau_{"+str(i)+"}}{M_{"+str(i)+"~"+str(j)+"}l_{"+str(i)+"}}"))
	# g -> g
	g = symbols('g')
	# l_{x} -> l[x]
	l = []
	for i in range(0,N+1):
		l.append(symbols("l_{"+str(i)+"}"))
	# \sin(\theta_x-\theta_y) -> si[x*(N+1)+y]
	si = []
	for i in range(0,N+1):
		for j in range(0,N+1):
			si.append(symbols("\\sin(\\theta_{"+str(i)+"}-\\theta_{"+str(j)+"})"))
	# \\dot\\theta_x -> v[x]
	v = []
	for i in range(0,N+1):
		v.append(symbols("\\dot\\theta_{"+str(i)+"}"))

def set_values_matlab():
	# cos(u[x]-u[y]) -> co[x*(N+1)+y]
	co = []
	for i in range(0,N+1):
		for j in range(0,N+1):
			co.append(symbols("cos(u["+str(i)+"]-u["+str(j)+"])"))
	# cos(u[x]) -> co1[x]
	co1 = []
	for i in range(0,N+1):
		co1.append(symbols("cos(u["+str(i)+"])"))
	# delta[x,y] -> d[x*(N+1)+y]
	d = []
	for i in range(0,N+1):
		for j in range(0,N+1):
			d.append(symbols("delta("+str(i)+"~"+str(j)+"~m)"))
	# tau[x]/(M[x,y]l[x]) -> \frac{\tau_x}{M_{x~y}l_{x}} -> F[x*(N+1)+y]
	F = []
	for i in range(0,N+1):
		for j in range(0,N+1):
			F.append(symbols("tau["+str(i)+"]/(M["+str(i)+"~"+str(j)+"~m]*l["+str(i)+"])"))
	# g -> g
	g = symbols('g')
	# l[x] -> l[x]
	l = []
	for i in range(0,N+1):
		l.append(symbols("l["+str(i)+"]"))
	# sin(u[x]-u[y]) -> si[x*(N+1)+y]
	si = []
	for i in range(0,N+1):
		for j in range(0,N+1):
			si.append(symbols("sin(u["+str(i)+"]-u["+str(j)+"])"))
	# v[x] -> v[x]
	v = []
	for i in range(0,N+1):
		v.append(symbols("v["+str(i)+"]"))
	return (co,co1,d,F,g,l,si,v)
print("\n\n")





# for i in range(0,N):
# 	sol = getVectorSol(rref(N,torque_matrix_sym(N)))[i]
# 	print(str(i+1) + ".)   " + str(eval("simplify("+sol+")")).replace("**","^") + "\n")

sol = getVectorSol(rref(N,torque_matrix_sym(N)))
# vals = set_values_matlab()
# co = vals[0]
# co1 = vals[1]
# d = vals[2]
# F = vals[3]
# g = vals[4]
# l = vals[5]
# si = vals[6]
# v = vals[7]
# print(sol)
# print(getVectorSol(rref_LaTeX(N,torque_matrix(N)))[N-1])
# print("\n")
# print(getVectorSol(rref_LaTeX(N,torque_matrix(N)))[N-1])

# simplification - redo



# for i in range(0,N):
# 	# sol = getVectorSol(rref(N,torque_matrix_sym(N)))[i]
# 	print(str(i+1) + ".)   " + str(eval("simplify("+sol[i]+")")).replace("**","^") + "\n")
# print("here")



#out to file:

# file = open("pendulum_output.txt","w")


for i in range(0,N):
	# file = open(f"pen_out_{N}_{i}.txt","w")

	# sol = getVectorSol(rref(N,torque_matrix_sym(N)))[i]
	# out = str(eval("simplify("+sol[i]+")"))

	out = str(sol[i])
	# out = out.replace('tau','F')
	out = out.replace("~",",").replace("[","(").replace("]",")")
	for j in range(0,N):
		out = out.replace(f"({j+1})",f"[{j}]")
	for j in range(0,N):
		out = out.replace(f"v[{j}]",f"u[{N+j}]")

	# for j in range(0,3*N+1):
	# 	out = out.replace(f"u[{j}]",f"mytemporary[{indexed+j}]")
	# out = out.replace("mytemporary",'u')



	print(out)
	print()

	# file.write(out)
	# file.close()



#out to cmd

# for i in range(0,N):
# 	# sol = getVectorSol(rref(N,torque_matrix_sym(N)))[i]
# 	# out = str(eval("simplify("+sol[i]+")"))
# 	out = str(sol[i])
# 	out = out.replace("~",",").replace("[","(").replace("]",")")
# 	for j in range(0,N):
# 		out = out.replace(f"({j+1})",f"[{j}]")
# 	for j in range(0,N):
# 		out = out.replace(f"v[{j}]",f"u[{N+j}]")
# 	print(out+",",end='')
# for i in range(0,N):
# 	# sol = getVectorSol(rref(N,torque_matrix_sym(N)))[i]
# 	out = str(eval("simplify("+sol[i]+")"))
# 	print(str(i+1) + ".)   " + out.replace("~",",").replace("**","^"))#.replace("(","\\left(").replace(")","\\right)").replace("*","\\cdot "))
# 	print("")
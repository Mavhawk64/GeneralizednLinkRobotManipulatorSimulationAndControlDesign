def torque_eq_alt(N,p):
	ret = "M_{" + str(p) + "," + str(N) + "}l_{"+str(p)+"}^2\\ddot\\theta_{"+str(p)+"}+"
	for j in range(1,p):
		ret += "M_{" + str(p) + "," + str(N) + "}l_{"+str(p)+"}l_{"+str(j)+"}\\ddot\\theta_{"+str(j)+"}\\cos(\\theta_{"+str(j)+"}-\\theta_{"+str(p)+"})-"
		ret += "M_{" + str(p) + "," + str(N) + "}l_{"+str(p)+"}l_{"+str(j)+"}\\dot\\theta_{"+str(j)+"}^2\\sin(\\theta_{"+str(j)+"}-\\theta_{"+str(p)+"})+"
	ret = ret[:-1] + "+"
	for n in range(p+1,N+1):
		ret += "M_{"+str(n)+","+str(N)+"}l_{"+str(p)+"}l_{"+str(n)+"}\\ddot\\theta_{"+str(n)+"}\\cos(\\theta_{"+str(p)+"}-\\theta_{"+str(n)+"})+"
		ret += "M_{"+str(n)+","+str(N)+"}l_{"+str(p)+"}l_{"+str(n)+"}\\dot\\theta_{"+str(n)+"}^2\\sin(\\theta_{"+str(p)+"}-\\theta_{"+str(n)+"})+"
	ret += "M_{"+str(p)+","+str(N)+"}l_{"+str(p)+"}g\\cos\\theta_{"+str(p)+"}=\\tau_{"+str(p)+"}"
	return ret

def torque_sys_eqs_alt(N):
	ret = "\\begin{cases}"
	for i in range(1,N+1):
		ret += torque_eq_alt(N,i)+"\\\\"
	ret += "\\end{cases}"
	return ret

def l_o_t(N,p):
	ret = "-"
	for j in range(1,p):
		ret += "M_{"+str(p)+","+str(N)+"}l_{"+str(p)+"}l_{"+str(j)+"}\\dot\\theta_{"+str(j)+"}^2\\sin(\\theta_{"+str(j)+"}-\\theta_{"+str(p)+"})-"
	ret = ret[:-1] + "+"
	for n in range(p+1,N+1):
		ret += "M_{"+str(n)+","+str(N)+"}l_{"+str(p)+"}l_{"+str(n)+"}\\dot\\theta_{"+str(n)+"}^2\\sin(\\theta_{"+str(p)+"}-\\theta_{"+str(n)+"})+"
	ret = ret[:-1]
	return ret

def low_order_terms(N):
	ret = "\\begin{bmatrix}"
	for i in range(1,N+1):
		ret += l_o_t(N,i) + "\\\\"
	ret += "\\end{bmatrix}"
	return ret

def m_matrix(N):
	ret = "\\begin{bmatrix}\n"
	for i in range(1,N+1):
		for j in range(1,N+1):
			if i == j:
				ret += "M_{" + str(i) + "," + str(N) + "}l_{" + str(i) + "}^2 & "
			elif i > j:
				ret += "M_{" + str(i) + "," + str(N) + "}l_{" + str(i) + "}l_{" + str(j) + "}\\cos(\\theta_{" + str(j) + "}-\\theta_{" + str(i) + "}) & "
			else:
				ret += "M_{" + str(j) + "," + str(N) + "}l_{" + str(i) + "}l_{" + str(j) + "}\\cos(\\theta_{" + str(i) + "}-\\theta_{" + str(j) + "}) & "
		ret = ret[:-2] + "\\\\\n"
	ret += "\\end{bmatrix}"
	return ret

def torque_m_matrix(N):
	ret = []
	for i in range(1,N+1):
		ret.append([])
		for j in range(1,N+1):
			if i == j:
				ret[i-1].append("M_{" + str(i) + "," + str(N) + "}l_{" + str(i) + "}^2")
			elif i > j:
				ret[i-1].append("M_{" + str(i) + "," + str(N) + "}l_{" + str(i) + "}l_{" + str(j) + "}\\cos(\\theta_{" + str(j) + "}-\\theta_{" + str(i) + "})")
			else:
				ret[i-1].append("M_{" + str(j) + "," + str(N) + "}l_{" + str(i) + "}l_{" + str(j) + "}\\cos(\\theta_{" + str(i) + "}-\\theta_{" + str(j) + "})")
	return ret

def dot_product(v,w):
	if len(v) != len(w):
		return None
	ret = ""
	for i in range(0,len(v)):
		ret += "\\left("+v[i]+"\\right)\\cdot\\left("+w[i]+"\\right) + "
	ret = ret[:-2]
	return ret

def P_I_D(N):
	ret = []
	for i in range(1,N+1):
		ret.append([])
		ret[i-1] = "K_{P_{" + str(i) + "}}(\\theta_{" + str(i) + "f}-\\theta_{" + str(i) + "})-K_{D_{" + str(i) + "}}\\dot\\theta_{" + str(i) + "}+K_{I_{" + str(i) + "}}x_{" + str(i) + "}"
	return ret

def P_I_D_LaTeX(N):
	ret = "\\begin{bmatrix}\n"
	for i in range(1,N+1):
		ret += "K_{P_{" + str(i) + "}}(\\theta_{" + str(i) + "f}-\\theta_{" + str(i) + "})-K_{D_{" + str(i) + "}}\\dot\\theta_{" + str(i) + "}+K_{I_{" + str(i) + "}}x_{" + str(i) + "} \\\\\n"
	ret += "\\end{bmatrix}"
	return ret

def torque_vector(N):
	ret = "\\begin{bmatrix}\n"
	m = torque_m_matrix(N)
	k = P_I_D(N)
	for i in range(1,N+1):
		ret += dot_product(m[i-1],k) + "\\\\\n"
	ret += "\\end{bmatrix}"
	return ret


# -------- PYTHON OUTPUT -------- #


# Returns (Python) code as an output of the torque vector (of form [[elem1],[elem2],[elem3],...])
def torque_vector_code_output(N,index=0):
	ret = '[\n'
	m = torque_m_matrix_code_output(N,index)
	k = P_I_D_Code_Output(N,index)
	for i in range(1,N+1):
		ret += '[' + dot_product_code_output(m[i-1],k) + '],\n'
	return ret[:-2] + '\n]'

def torque_m_matrix_code_output(N,index=0):
	ret = []
	for i in range(1,N+1):
		ret.append([])
		for j in range(1,N+1):
			if i == j:
				ret[i-1].append("M(" + str(i) + "," + str(N) + ",m)*l[" + str(i+index-1) + "] ** 2")
			elif i > j:
				ret[i-1].append("M(" + str(i) + "," + str(N) + ",m)*l[" + str(i+index-1) + "]*l[" + str(j+index-1) + "]*cos(u[" + str(N+j+index-1) + "]-u[" + str(N+i+index-1) + "])")
			else:
				ret[i-1].append("M(" + str(j) + "," + str(N) + ",m)*l[" + str(i+index-1) + "]*l[" + str(j+index-1) + "]*cos(u[" + str(N+i+index-1) + "]-u[" + str(N+j+index-1) + "])")
	return ret
def P_I_D_Code_Output(N,index):
	ret = []
	for i in range(1,N+1):
		ret.append([])
		ret[i-1] = "KP[" + str(i+index-1) + "]*(thetaf[" + str(i+index-1) + "]-u[" + str(N+i+index-1) + "])-KD[" + str(i+index-1) + "]*u[" + str(2*N+i+index-1) + "]+KI[" + str(i+index-1) + "]*u[" + str(i+index-1) + "]"
	return ret

def dot_product_code_output(v,w):
	if len(v) != len(w):
		return None
	ret = ""
	for i in range(0,len(v)):
		ret += "("+v[i]+")*("+w[i]+") + "
	ret = ret[:-3]
	return ret


# LaTeX Output
# print(torque_m_matrix(4))
# print(P_I_D_LaTeX(2))
# print(torque_vector(2))
# print(torque_sys_eqs_alt(2))
# print(dot_product(['0','3','5'],['3','4','3']))

# Python Output
print(torque_vector_code_output(2,1))
# print(torque_m_matrix(2))
# print(P_I_D(2))
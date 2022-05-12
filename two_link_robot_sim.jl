### A Pluto.jl notebook ###
# v0.19.3

using Markdown
using InteractiveUtils

# ╔═╡ 4b8fa450-d170-11ec-3b73-470a743cceb2
begin
	function M(x,y,m)
		s = 0
		for j in x:y
			s += m[j]
		end
		return s
	end
end

# ╔═╡ cac26ec0-9066-44ff-b8dd-bfa6bf513660
begin
	function delta(p,n,m)
		return M(n,length(m),m) / M(p,length(m),m)
	end
end

# ╔═╡ c4b00865-8476-46af-8095-4857ebe6f5e7
begin
	function c(p,N,l,m,theta,dottheta)
		cp = 0
		for n in p+1:N
			cp += M(n,N,m) * l[p] * l[n] * dottheta[n] * dottheta[n] * sin(theta[p] - theta[n])
		end
		for j in 1:p-1
			cp -= M(p,N,m) * l[p] * l[j] * dottheta[j] * dottheta[j] * sin(theta[j] - theta[p])
		end
		return cp
	end
end

# ╔═╡ 3547221a-d857-4af6-8ddb-0b9a823be298
begin
	function G(p,N,l,m,g,theta)
		return M(p,N,m) * l[p] * g * cos(theta[p])
	end
end

# ╔═╡ 35d278b0-a543-4a64-859c-21a38bf83b45
begin
	# This is the element calculation of the M(Theta) matrix.
	# x is the column, y is the row
	function Mtrx(x,y,N,l,m,theta)
		if x == y
			return M(x,N,m) * l[x] * l[x]
		end
		if x < y
			return M(y,N,m) * l[x] * l[y] * cos(theta[x] - theta[y])
		end
		return M(x,N,m) * l[y] * l[x] * cos(theta[y] - theta[x])
	end
end

# ╔═╡ 8deb80be-40a8-4310-a39a-3e73bc21192b
begin
	u = [1,2,3,4,5,6]
	g = 0.01
	l = [2,1]
	m = [1,1]
	KP = [30,30]
	KD = [15,10]
	KI = [20,20]
	thetaf = [3.1415926535897932384626 / 2,0]
	F = [
(M(1,2,m)*l[1] ^ 2)*(KP[1]*(thetaf[1]-u[3])-KD[1]*u[5]+KI[1]*u[1]) + (M(2,2,m)*l[1]*l[2]*cos(u[3]-u[4]))*(KP[2]*(thetaf[2]-u[4])-KD[2]*u[6]+KI[2]*u[2]),
(M(2,2,m)*l[2]*l[1]*cos(u[3]-u[4]))*(KP[1]*(thetaf[1]-u[3])-KD[1]*u[5]+KI[1]*u[1]) + (M(2,2,m)*l[2] ^ 2)*(KP[2]*(thetaf[2]-u[4])-KD[2]*u[6]+KI[2]*u[2])
]
end

# ╔═╡ ae01d6fb-f9d5-4147-9c09-36fb7f6c88a9
c(1,2,l,m,u[3:4],u[5:6])

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

julia_version = "1.7.2"
manifest_format = "2.0"

[deps]
"""

# ╔═╡ Cell order:
# ╠═4b8fa450-d170-11ec-3b73-470a743cceb2
# ╠═cac26ec0-9066-44ff-b8dd-bfa6bf513660
# ╠═c4b00865-8476-46af-8095-4857ebe6f5e7
# ╠═3547221a-d857-4af6-8ddb-0b9a823be298
# ╠═35d278b0-a543-4a64-859c-21a38bf83b45
# ╠═8deb80be-40a8-4310-a39a-3e73bc21192b
# ╠═ae01d6fb-f9d5-4147-9c09-36fb7f6c88a9
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002

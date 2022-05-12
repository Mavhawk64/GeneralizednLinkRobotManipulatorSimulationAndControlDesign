function delta = delta(p,n,m)
M = @M;
delta = M(n,length(m),m) / M(p,length(m),m);
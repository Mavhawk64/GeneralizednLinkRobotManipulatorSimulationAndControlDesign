function M = M(x,N,m)
M = 0;
for i = x:N
    M = M + m(i);
end
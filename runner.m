h = 0.1;
g = 0.01;
t = 0;
m = [1,1];
l = [1,1];
tau = [0,0];
delta = @delta;
u = [0,0,0,0]';
o = [u];
for i = 1:100
    S = [u(3),u(4),(cos(u(1))*g - cos(u(1)-u(2))*cos(u(2))*delta(1,2,m)*g + cos(u(1)-u(2))*delta(1,2,m)*l(1)*sin(u(1)-u(2))*u(3)^2 + cos(u(1)-u(2))*delta(1,2,m)*tau(2)/(M(2,2,m)*l(2)) + delta(1,2,m)*l(2)*sin(u(1)-u(2))*u(4)^2 - tau(1)/(M(1,2,m)*l(1)))/(l(1)*(cos(u(1)-u(2))^2*delta(1,2,m) - 1)),(-cos(u(1)-u(2))*(cos(u(1))*g + delta(1,2,m)*l(2)*sin(u(1)-u(2))*u(4)^2 - tau(1)/(M(1,2,m)*l(1))) + cos(u(2))*g - l(1)*sin(u(1)-u(2))*u(3)^2 - tau(2)/(M(2,2,m)*l(2)))/(l(2)*(cos(u(1)-u(2))^2*delta(1,2,m) - 1))]';
    u = u + h * S
    %o(i+1)=u;
end



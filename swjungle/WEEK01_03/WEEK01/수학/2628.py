import sys

w, h = map(int,sys.stdin.readline().split())

x = []
y = []

for i in range(int(sys.stdin.readline())):
    d, o = map(int,sys.stdin.readline().split())
    if d == 0:
        y.append(o)
    else:
        x.append(o)

x.sort()
y.sort()

if len(x)!=0:
    w_fag = [x[0],w-x[-1]]
else:
    w_fag = [w]
if len(y)!=0:
    h_fag = [y[0],h-y[-1]]
else:
    h_fag = [h]

for i in range(len(x)-1):
    w_fag.append(x[i+1]-x[i])
for i in range(len(y)-1):
    h_fag.append(y[i+1]-y[i])

print(max(w_fag)*max(h_fag))
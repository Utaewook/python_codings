import matplotlib.pyplot as plt

plt.xlabel("x")
plt.ylabel("Y")

x1, y1, x2, y2 = map(int, input().split())

if (x1 <= x2):
    dy = y2 - y1
    dx = x2 - x1
    if(dy/dx<=1):
        
        x = x1
        y = y1
        d = dy - (dx / 2)  # d start
        xset = [x]
        yset = [y]

        while (x < x2):
            x = x + 1
            if (d > 0):
                d = d + (dy - dx)
                y = y + 1
            else:
                d = d + dy
            xset.append(x)
            yset.append(y)
    else:
        #기울기가 1보다 크고 x1<=x2일때
         x = x1
         y = y1
         d = dy - (dx / 2)  # d start
         xset = [y]
         yset = [x]

         while (x < x2):
            x = x + 1
            if (d > 0):
                d = d + (dy - dx)
                y = y + 1
            else:
                d = d + dy
            xset.append(y)
            yset.append(x)
            
plt.scatter(x=xset,y=yset)
plt.show()
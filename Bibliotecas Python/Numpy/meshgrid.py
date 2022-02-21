from pylab import scatter
from numpy import array

#------------------------------------------------
x = array([1, 1.2, 1, 1.2, 1, 1.2])
y = array([-0.5, 2, 2, -0.5, -0.2, -0.2])

scatter(x,y,
       marker = '+',
       color = 'green')

#------------------------------------------------

from numpy import meshgrid

ValoresX = array([complex(1,0), complex(1.2, 0)])
ValoresY = array([complex(0, -0.5), complex(0, -0.2), complex(0,2)])

XX, YY = meshgrid(ValoresX, ValoresY)

ZZ = XX + YY

#------------------------------------------------------

X = array([1,1.2])
Y = array([-0.5, -0.2, 2])

xx, yy = meshgrid(X, Y)

scatter(xx, yy,
        color = 'green',
        marker = '+')

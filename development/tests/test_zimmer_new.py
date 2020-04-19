import numpy as np
from synergy.combination import ZimmerNew
from synergy.utils.dose_tools import grid


h1, h2 = 2.3, 0.8
C1, C2 = 1e-2, 1e-1
a12, a21 = -1., 1.
npoints = 10

truemodel = ZimmerNew(h1=h1, h2=h2, C1=C1, C2=C2, a12=a12, a21=a21)

D1, D2 = grid(1e-3, 1, 1e-2, 1, npoints, npoints)
E = truemodel._model(D1, D2, h1, h2, C1, C2, a12, a21)



Efit = E*(1+(np.random.rand(len(D1))-0.5)/4.)

model = ZimmerNew()
model.fit(D1, D2, Efit, bootstrap_iterations=100)
print(model)
print(model.get_parameter_range().T)
from divi import diviner
from masser import between as bt
from small_function.normalizеr import normalize

dv = diviner.Divine()
sings = ['+', '-', '*', '/']
dv.sing = ''.join(sings)
nb = dv.div("23-x*8-5=1")
print(nb)

count = sum(list(map(nb.count, sings)))
print(count)
print(bt.between(nb, ['-', '*'], radius=2, side="right"))


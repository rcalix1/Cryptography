
## >> pip install randomgen

from numpy.random import Generator
from randomgen import ChaCha
from randomgen import AESCounter

rg = Generator(AESCounter(12345, mode="Sequence"))

## rg = [ Generator(ChaCha(1234)) for _ in range(10) ]
print(rg)

for i in range(10):
    res = rg.random() * 1000
    print(int(res))

from Crypto.PublicKey import RSA
from Crypto.Util.number import *

with open('pub.pem', 'r') as f:
    key = RSA.importKey(f.read())
    n = key.n
    e = key.e
    print(n, e)
print(long_to_bytes(n))

c = "??"
from factordb.factordb import FactorDB

f = FactorDB(n)
f.connect()
print(f.get_factor_list())
p,q = f.get_factor_list()
d = inverse(e,(p-1)*(q-1))
m = pow(c,d,n)
print(long_to_bytes(m))

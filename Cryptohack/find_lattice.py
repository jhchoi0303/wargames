#https://blog.csdn.net/qq_33458986/article/details/104366177
from Crypto.Util.number import long_to_bytes, inverse
from math import floor

def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m


class vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def mul(u, v):
    r = u.x * v.x + u.y * v.y
    return r
def multiple(k, a):
    x = k * a.x
    y = k * a.y
    u = vec(x, y)
    return u
def sub(u, v):
    x = u.x - v.x
    y = u.y - v.y
    r = vec(x, y)
    return r

def Gaussia(v, u):
    while True:
        if mul(u, u) < mul(v, v):
            t = u
            u = v
            v = t
        m = floor(mul(v, u) / mul(v, v))
        if m == 0:
            break
        else:
            u = sub(u, multiple(m, v))
    return (v, u)

q, h = (7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257, 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800)
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523
v = vec(1, h)
u = vec(0, q)
v, u = Gaussia(v, u)
f = v.x
g = v.y
print(long_to_bytes(decrypt(q, h, f, g, e)).decode())

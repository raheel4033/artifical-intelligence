import hashlib as h

n = h.sha3_256()
n.update(b'This is my Proof of work example')
n.digest()
n.hexdigest()

print(n.digest())
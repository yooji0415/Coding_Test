import hashlib
import sys

s = sys.stdin.readline().strip()
result = hashlib.sha256(s.encode())
print(result.hexdigest())

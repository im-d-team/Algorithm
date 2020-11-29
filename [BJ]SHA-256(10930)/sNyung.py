import hashlib
from sys import stdin

def hash_string(string):
  return hashlib.sha256(string.encode('utf-8')).hexdigest()

string = str(input())
print(hash_string(string))
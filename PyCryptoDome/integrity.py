
from Crypto.Hash import MD5

m = MD5.new()

string_value = 'buy the stock at $2500 a share'
spoofed_string_value = 'buy the stock at $1500 a share'

m.update(string_value)
print m.digest()
m_hash_value = m.hexdigest()

n = MD5.new()
n.update(spoofed_string_value)

n_hash_value = n.hexdigest()

if m_hash_value == n_hash_value:
    print True
else:
    print False

import hashlib
import collections

def hash(value):
  def hash_item(item): return hashlib.md5(item.encode()).hexdigest()

  if (isinstance(value, dict)):
    return { key: hash_item(val) for key, val in value.items() }

  if (isinstance(value, str)):
    return hash_item(value)

  try:
    return list(map(hash_item, value))
  except TypeError:
    return hash_item(value.encode())

print(hash('hello'))
print(hash(['hello', 'my', 'firend']))
print(hash({ 'message': 'hello' }))
  
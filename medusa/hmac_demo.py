import hmac

ENCODING_TYPE = 'utf-8'

key = 'secret'
msg = 'haha'

h = hmac.new(key.encode(ENCODING_TYPE), msg.encode(ENCODING_TYPE), digestmod='SHA256')
r = h.hexdigest()

print(r)


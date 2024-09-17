
import json

##jsoninjson
import jwts
username='123", "admin": "True'

body = '{' \
              + '"admin": "' + "False" \
              + '", "username": "' + str(username) \
              + '"}'

print(json.loads(body))

#{"response":"Welcome admin, here is your flag: crypto{https://owasp.org/www-community/Injection_Theory}"}
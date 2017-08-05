import requests
import json
from AccessToken import ACCESS_TOKEN
BASE_URL="https://api.instagram.com/v1/"

class Owner:
    def __init__(self):
        return None
    def get_self_info(self):
        get_url=BASE_URL+"users/self/?access_token="+ACCESS_TOKEN
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "owner object can not be accessed"
        if user_info['meta']['code']==200:
            print"\nName:",user_info['data']['full_name']
            print"\nID:",user_info['data']['id']
            print"\nProfile_Picture:",user_info['data']['profile_picture']
            print"\nFollows:",user_info['data']['counts']['follows']
            print"\nFollowed_by:",user_info['data']['counts']['followed_by']
        else:
            print"Request not successful"
        



class Users:
    def __init__(self):
        return None
    
    def get_id(self,user_name):
        
        get_url=(BASE_URL+"users/search?q=%s&access_token=%s")%(user_name,ACCESS_TOKEN)
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "owner object can not be accessed"
        
        if user_info['meta']['code']==200:
            if len(user_info['data']):
                return user_info['data'][0]['id']
            else:
                print"No user found of this name"
                return None
        else:
            print 'Request not successful'


    def show_Info(self,ID):
        
        get_url=(BASE_URL+"users/search?q=%s&access_token=%s")%(ID,ACCESS_TOKEN)
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "owner object can not be accessed"
        
        if user_info['meta']['code']==200:
            if len(user_info['data']):
                print"\nName:",user_info['data'][0]['full_name']
                print"\nID:",user_info['data'][0]['id']
                print"\nProfile_Picture:",user_info['data'][0]['profile_picture']
            else:
                print"no data for the user"
        else:
            print 'Request not successful'



    def get_post(self,ID):
        get_url=BASE_URL+"users/%s/media/recent/?access_token=%s"%(ID,ACCESS_TOKEN)
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "owner object can not be accessed"
        
        if user_info['meta']['code']==200:
            if len(user_info['data']):
                print(json.dumps(user_info["data"], indent=3))
                
            else:
                print"no data for the user"
        else:
            print 'Request not successful'



    def get_comments(self,ID):

        get_url=BASE_URL+"users/%s/media/recent/?access_token=%s"%(ID,ACCESS_TOKEN)
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "owner object can not be accessed"
        
        mediaID1=user_info["data"][0]['id']
        mediaID2=user_info["data"][1]['id']
        inp=int(raw_input("\n1.for most recent post\n2.for second most recent post"))
        if inp==1:
            get_url=BASE_URL+"media/%s/comments?access_token=%s"%(mediaID1,ACCESS_TOKEN)
        else:
            get_url=BASE_URL+"media/%s/comments?access_token=%s"%(mediaID2,ACCESS_TOKEN)
        
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "owner object can not be accessed"
        
        if user_info['meta']['code']==200:
            if len(user_info['data']):
                for i in range(0,len(user_info['data'])):
                    print"Comment:",i+1,user_info['data'][i]['text']
                
            else:
                print"no comment on this post"
        else:
            print 'Request not successful' 
        

while(True):
    choice=int(raw_input("\n1.to show owner info\n2.to show other user info\n3.exit\n"))
    if choice==3:
        exit()
    elif choice==1: #owners comment and post need to be done
        owner_obj=Owner()
        owner_obj.get_self_info()
    elif choice==2:
        while True:
            print"please select user:"
            select=int(raw_input("\n1.legenwait4itdary\n2.divyesh.712"))
            if select==1:
                UserName="legenwait4itdary"
                break
            elif select==2:
                UserName="divyesh.712"
                break
            else:
                print "wrong input try again"
        Users_obj=Users()
        ID=Users_obj.get_id(UserName)
        while True:
            choice_1=int(raw_input("\n1.to show " +UserName+ " info\n2.to show " +UserName+  " post\n3.to show "+UserName+ " comment\n"))
            if choice_1==1:
                Users_obj.show_Info(UserName)
                break
            elif choice_1==2:
                Users_obj.get_post(ID)
                break
            elif choice_1==3:
                Users_obj.get_comments(ID)

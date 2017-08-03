import requests
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
        print get_url
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
        
        get_url=(BASE_URL+"/users/%s/?access_token=%s")%(ID,ACCESS_TOKEN)
        #print get_url
        

while(True):
    choice=int(raw_input("\n1.to show owner info\n2.to show other user info\n3.exit\n"))
    if choice==3:
        exit()
    elif choice==1:
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
            choice_1=int(raw_input("\n1.to show info\n2.to show post\n3.to show comment\n"))
            if choice_1==1:
                Users_obj.show_Info(ID)
        

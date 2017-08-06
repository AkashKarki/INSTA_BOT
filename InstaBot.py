import requests
import json
import collections
import operator
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
            return None
        if user_info['meta']['code']==200:
            print"\nName:",user_info['data']['full_name']
            print"\nID:",user_info['data']['id']
            print"\nProfile_Picture:",user_info['data']['profile_picture']
            print"\nFollows:",user_info['data']['counts']['follows']
            print"\nFollowed_by:",user_info['data']['counts']['followed_by']
        else:
            print"Request not successful"


    def recent_media_liked(self):
        
        get_url=BASE_URL+"users/self/media/liked?access_token="+ACCESS_TOKEN
        
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "owner object can not be accessed"
            return None
        if user_info['meta']['code']==200:
            if len(user_info["data"]):
                print (json.dumps(user_info["data"], indent=3))
            else:
                print"NO recently liked data"
        else:
            print"Request not successful"


    def get_post(self):
        get_url=BASE_URL+"users/self/media/recent/?access_token="+ACCESS_TOKEN
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "owner object can not be accessed"
            return None
        if user_info['meta']['code']==200:
            if len(user_info["data"]):
                print (json.dumps(user_info["data"], indent=3))
            else:
                print"NO posts"
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
            print "object can not be accessed"
            return None
        
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
            print "object can not be accessed"
            return None
        
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
            print "object can not be accessed"
            return None

        inp=int(raw_input("\n1.to show/select post with minimum Like\n2.to show/select post with maximum Like\n3.to show/select post with perticular caption\n"))
        if user_info['meta']['code']==200:
            if len(user_info['data']):
                if inp==1:
                    like=9999999
                    postID=""
                    
                    for i in range(0,len(user_info["data"])):
                        if int(user_info["data"][i]['likes']['count'])<like:
                            like=int(user_info["data"][i]['likes']['count'])
                            postID=user_info["data"][i]['id']
                    get_url=BASE_URL+"media/%s?access_token=%s"%(str(postID),ACCESS_TOKEN)
                    try:
                        user_info = requests.get(get_url).json()
                    except Exception as e:
                        print "object can not be accessed"
                        return None
                    if user_info['meta']['code']==200:
                        if len(user_info['data']):
                            print (json.dumps(user_info["data"], indent=3))
                            return str(postID)
                        else:
                            print"No post found"
                            return None
                    else:
                        print 'Request not successful'
                        return None
                elif inp==2:
                    like=0
                    postID=""
                    
                    for i in range(0,len(user_info["data"])):
                        if int(user_info["data"][i]['likes']['count'])>like:
                            like=int(user_info["data"][i]['likes']['count'])
                            postID=user_info["data"][i]['id']
                    get_url=BASE_URL+"media/%s?access_token=%s"%(str(postID),ACCESS_TOKEN)
                    try:
                        user_info = requests.get(get_url).json()
                    except Exception as e:
                        print "object can not be accessed"
                        return None
                    if user_info['meta']['code']==200:
                        if len(user_info['data']):
                            print (json.dumps(user_info["data"], indent=3))
                        else:
                            print"No post found "
                            return None
                    else:
                        print 'Request not successful'
                elif inp==3:
                    cap=raw_input("enter the caption")
                    postID=list()
                    for i in range(0,len(user_info["data"])):
                        if user_info["data"][i]['caption']['text']==cap:
                            postID.append(user_info["data"][i]['id'])
                    if  len(postID):
                        for Id in postID:
                          get_url=BASE_URL+"media/%s?access_token=%s"%(str(Id),ACCESS_TOKEN)
                          try:
                                user_info = requests.get(get_url).json()
                          except Exception as e:
                                print "object can not be accessed"
                                return None
                    if user_info['meta']['code']==200:
                        if len(user_info['data']):
                            print (json.dumps(user_info["data"], indent=3))
                        else:
                            print"No post found"
                            return None
                    else:
                        print 'Request not successful'
                
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
        inp=int(raw_input("\n1.for comments on most recent post\n2.for comments on second most recent post"))
        if inp==1:
            get_url=BASE_URL+"media/%s/comments?access_token=%s"%(mediaID1,ACCESS_TOKEN)
            print get_url
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


    def like_user_post(self,user_id):
        obj=Users()
        media_id = obj.get_post(user_id)
        if media_id!=None:
            print"***************POSTING LIKE ON MEDIA****************"
            post_url = BASE_URL+ 'media/%s/likes' % (media_id)
            payload = {"access_token": ACCESS_TOKEN}
            post_a_like = requests.post(post_url, payload).json()
            if post_a_like["meta"]["code"] == 200:
                print "\nThe post has been Liked.\n"
            else:
                print "\nYour like was unsuccessful on the post. Please Try again\n"
        
        else:
            print"media ID not found"


    def comment_user_post(self,user_id):
        obj=Users()
        media_id = obj.get_post(user_id)
        print"***************POSTING COMMENT ON MEDIA****************"
        if media_id!=None:
            comment=raw_input("Enter the comment you want to post: ")
            payload = {"access_token": ACCESS_TOKEN, "text" : comment}
            post_url = BASE_URL+ "media/%s/comments" % (media_id)
            post_comment = requests.post(post_url, payload).json()
            if post_comment['meta']['code'] == 200:
                print "\nSuccessfully added the comment!\n"
            else:
                print "\nUnable to add the comment. Please try again!"
        else:
            print"media ID not found"



    def marketing(self,ID):
        markiting_items=['food','tshits','shoes','coffee','clothes','movies','Music','laptop','technology','car','bike','mobile','pet','LoveTravelling','dog','cat']
        get_url=BASE_URL+"users/%s/media/recent/?access_token=%s"%(ID,ACCESS_TOKEN)
        try:
            user_info = requests.get(get_url).json()
        except Exception as e:
            print "object can not be accessed"
        
        if user_info['meta']['code']==200:
            caption_list=list()
            if len(user_info['data']):
                for i in range(0,len(user_info['data'])):
                   cap=user_info["data"][i]['caption']['text']
                   cap=cap.split('#')
                   caption_list=caption_list+cap
                caption_list2=collections.Counter(caption_list)
                caption_list2=sorted(caption_list2.items(), key=operator.itemgetter(1),reverse=True)
                i=0
                fav_list=list()
                for key in caption_list2:
                    fav_list.append(key)
                    i=i+1
                    if i==5:
                        break
                fav_list=dict(fav_list)
                fav_item=list()
                for key in fav_list.keys():
                    fav_item.append(key)
                caption_list=' '.join(caption_list)
                caption_list=caption_list.split(' ')
                for items in caption_list:
                    if items in markiting_items:
                        fav_item.append(items)
                print"*****************prouct that are liked by users are*****************"
                for items in fav_item:
                    print"=>",items
            else:
                print"NO post found"
        else:
            print"Unable to process request code other than 200"
while(True):
    choice=int(raw_input("\n1.to show owner info\n2.to show other user info\n3.Marketing your Product\n4.exit\n"))
    if choice==4:
        exit()
    elif choice==1:
        inps=int(raw_input("\n1.to show owner basic info\n2.to show owners posts\n3.show recent media liked by user\n"))
        owner_obj=Owner()
        if inps==1:
            owner_obj.get_self_info()
        elif inps==2:
            owner_obj.get_post()
        elif inps==3:
            owner_obj.recent_media_liked()
        else:
            print"wrong input"
    
    elif choice==2:
        while True:
            print"please select user:"
            select=int(raw_input("\n1.legenwait4itdary\n2.divyesh.712\n3.shiven.basnet"))
            if select==1:
                UserName="legenwait4itdary"
                break
            elif select==2:
                UserName="shiven.basnet"
                break
            else:
                print "wrong input try again"
        Users_obj=Users()
        ID=Users_obj.get_id(UserName)
        while True:
            choice_1=int(raw_input("\n1.to show " +UserName+ " info\n2.to show " +UserName+  " posts\n3.to show "+UserName+ " comments on a post\n4.to like a post of "+UserName+"\n5.to comment on a post of"+UserName+"\n"))
            if choice_1==1:
                Users_obj.show_Info(UserName)
                break
            elif choice_1==2:
                ids=Users_obj.get_post(ID)
                break
            elif choice_1==3:
                Users_obj.get_comments(ID)
                break
            elif choice_1==4:
                Users_obj.like_user_post(ID)
                break
            elif choice_1==5:
                Users_obj.comment_user_post(ID)
                break
    elif choice==3:
            print"please select user to whom you want to market the product:"
            select=int(raw_input("\n1.legenwait4itdary\n2.shiven.basnet"))
            if select==1:
                UserName="legenwait4itdary"
                
            elif select==2:
                UserName="shiven.basnet"
            
            else:
                print "wrong input try again"
            Users_obj=Users()
            ID=Users_obj.get_id(UserName)
            if ID!=None:
                Users_obj.marketing(ID)

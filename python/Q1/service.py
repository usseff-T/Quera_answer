from material import TrafficUsageDao
import math
from collections import defaultdict

class TrafficUsageService:
    def __init__(self, traffic_usage_dao: TrafficUsageDao):
        self.traffic_usage_dao = traffic_usage_dao

    def social_media_lovers(self, year: int, month: int):

        all_users=self.traffic_usage_dao.load_all()
        # self.get_usage_user(all_users)
        all_user_date=self.get_user_date(year,month,all_users)
        percent=math.ceil(len(all_user_date)*0.9)
        user_90=all_user_date[:percent]

        user_win=[]
        for user_main,total1 in self.get_usage_user_exteranl(all_user_date).items():
            # users_1[user]=total
            user_win.append(user_main)
            # print(total1,user_main)
            for user_9,total in self.get_usage_user_exteranl(user_90).items():
                # print(user_9)
                # print(total)
                # if user_main is not user_9:
                    if total1 < total:
                        # print(user_main)
                        break
            break

                        # print(user_main)
                # users_2[user]=total
        # print(user_win)
        return  user_win


    def none_check(self,listt):
        list_=[]
        for i in listt:
            if type(i)is not type(None):
                list_.append(i)
        return list_
    def get_user_date(self,year: int, month: int,users):
        recive_date=str(year)+"/"+"0"+str(month)
        user_d=[]
        for user_date in users:
            if not user_date.date.find(recive_date) and type(user_date.date) is not type(None):
                        user_d.append(user_date)
        return user_d

    def get_usage_user_exteranl(self,users):
        user_usage=defaultdict(int)
        for user in users:
            if not user.internal:
                user_usage[user.user.username]+=user.usage
        return user_usage

    def split_date(self,date_string):
        s_date=date_string.split('/')
        return  s_date[0]+"/"+s_date[1]

    def get_users_usage_internal(self,users):
        user_usage=defaultdict(int)
        for user in users:
            if user.internal:
                user_usage[user.user.username]+=user.usage
        return user_usage

    def download_lovers(self, year: int, month: int):
        all_users=self.traffic_usage_dao.load_all()
        all_users_date=self.get_user_date(year,month,all_users)
        index=0
        for user,total_external in self.get_usage_user_exteranl(all_users_date).items():
            user_interal=list(self.get_users_usage_internal(all_users_date).values())[index]
            index+=1
            if total_external > user_interal:
                print(user)
        # pass
        return []

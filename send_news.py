import itchat
from apscheduler.schedulers.blocking import BlockingScheduler


itchat.auto_login(hotReload=True)


def my_job():
    print('hello world')
    user_name = itchat.search_friends('老傅')[0]['UserName']
    itchat.send_file('fazhoubao.xlsx', toUserName=user_name)


scheduler = BlockingScheduler()
# scheduler.add_job(my_job, 'interval', seconds=5)
scheduler.add_job(my_job, 'cron', day='*', hour='18', minute='30')
scheduler.start()


# itchat.send('Hello, filehelper', toUserName='filehelper')


print('发送成功')

import time

import schedule


def job():
    print("I'm working...")


schedule.every(3).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("22:33").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

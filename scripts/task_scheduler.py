import schedule
import time


schedule.every().day.at("10:00").do(lambda: print("Task executed (every day at 10:00)"))
schedule.every().minute.do(lambda: print("Task executed every minute"))
schedule.every().second.do(lambda: print("Task executed every second"))

while 1:
    schedule.run_pending()
    time.sleep(1)

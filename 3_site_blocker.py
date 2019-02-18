import time
from datetime import datetime as dt

host_path = "c:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.netflix.com", "www.facebook.com"]

while True:
    now = dt.now()
    if dt(now.year, now.month, now.day, 8) < now < dt(now.year, now.month, now.day, 16):
        print("Working time!")

        # file = open(host_path, "r+")
        # content = file.read()
        #
        # for website in website_list:
        #     if website in content:
        #         pass
        #     else:
        #         file.write(redirect + " " + website + "\n")
        #         pass
    else:
        print("Free time")

        # file = open(host_path, "r+")
        # content = file.readlines()
        # file.seek(0)
        # for line in content:
        #     if not any(website in line for website in website_list):
        #         file.write(line)
        #     file.truncate()

    time.sleep(5)
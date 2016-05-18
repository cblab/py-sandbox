import webbrowser
import time

count = 0

print ("breaktaker started" + time.ctime())

while count < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=evkz3hgHQyM")
    count = count + 1

print "Breaktaker stopped - Good bye!"


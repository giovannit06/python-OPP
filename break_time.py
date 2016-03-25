import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime()) # print current time
while(break_count < total_breaks):
    time.sleep(10)  # time in seconds to change in the final version
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count = break_count + 1

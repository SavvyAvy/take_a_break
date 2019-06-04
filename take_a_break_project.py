import webbrowser
import time

total_turns = 3
turn = 0

print("This program started on" + time.ctime() )
while( turn < total_turns) :
    time.sleep(10)
    print("Time after program loop of 10 seconds " + time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=FngDSOuCNAA")
    turn = turn + 1
    
   

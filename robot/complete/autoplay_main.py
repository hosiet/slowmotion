import sqlite3
import sched, time
import threading
#import keyboardplay

conn=sqlite3.connect("smusic/new.db")
c=conn.cursor()
for x in c.execute("SELECT time,note FROM music"):
    pass
t=x[0].split()
w=x[1].split()
conn.close()

def kp_play_note_once(inputnote):
	#os.system('echo {0}={1} >> /dev/pi-blaster'.format(keyboardplay.keyboard_data[inputnote]['gpio'], keyboardplay.keyboard_data[inputnote]['low']))
	print(inputnote)
def strike_():
    s = sched.scheduler(time.time, time.sleep)
    count=-1
    for i in t:
        count+=1
        floatnumber = float(t[count])
        s.enter(floatnumber, 1,kp_play_note_once,argument=(w[count],))
    s.run()

class start_strike(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        strike_()
def test():
    thread1 = start_strike()
    thread1.start()
    thread1.join()

if __name__ == '__main__':
    test()
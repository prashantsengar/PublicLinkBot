import os
import threading

def tl():
  os.system('python -m tl')
def play():
  os.system('python play.py')

t= threading.Thread(target=tl)
p = threading.Thread(target=play)
t.start()
# p.start()
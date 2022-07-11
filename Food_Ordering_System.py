import threading
import time
import collections

class FoodOrder:
    def placeOrder(self):
        global orders
        global order_q
        for o in orders:
            order_q.append(o)
            print('order placed for '+ o)
            time.sleep(0.5)
        return 
    def serveOrder(self):
        global order_q
        time.sleep(1)
        while order_q:
            served = order_q.popleft()
            print('served order '+served)
            time.sleep(2)
        return
    

f = FoodOrder()
orders = ['pizza','samosa','pasta','biryani','burger']
order_q = collections.deque()
f.t1 = threading.Thread(target = f.placeOrder)
f.t2 = threading.Thread(target = f.serveOrder)
f.t1.start()
f.t2.start()


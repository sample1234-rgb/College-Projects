'''
global cost,visited
visited=[]
cost=[]
def initial(n):
    global visited,cost
    for i in range(n):
        arr=[]
        varr= []
        for j in range(n):
            arr.append(0)
            varr.append(False)
        # mat.append(arr)
        cost.append(arr)
        visited.append(varr)
# mat=[[0, 0, 0, 0, 0],
#      [1, 1, 1, 1, 0],
#      [2, 2, 2, 8, 0],
#      [1, 1, 1, 0, 0],
#      [0, 0, 0, 0, 0]]
def printMat(mat):
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=" ")
        print("\n")
def Maximum(mat_arr,visit_arr,cost_arr):
    max=mat_arr[0][0]
    for i in range(n):
        for j in range(n):
            if not visit_arr[i][j]:
                if((i-1) >= 0) and ((j-1) >= 0):
                    cost_arr[i][j] = cost_arr[i-1][j-1] + mat_arr[i][j]
                else:
                    cost_arr[i][j] = mat_arr[i][j]
                visit_arr[i][j] = True
            if(max < cost[i][j]):
                max=cost[i][j]
    print(max)
    printMat(cost_arr)
# printMat(mat)
# printMat(visited)
if __name__ is "__main__":
    t = int(input())
    while(t != 0):
        n = int(input())
        initial(n)
        mat = list()
        printMat(mat)
        t -= 1
'''
'''
# KICK_START:
st = input()
kcnt=0
scnt=0
cnt=0
lenk=0
lens=0
leng = len(st)
for i in range(leng):
    if st[i] == 'K':
        lenk=1
        for j in range(i+1,leng):
            if (st[j] == 'K'and st[j-2] == 'I' and st[j-1] == 'C'):
                kcnt += 1
                # k=j
                lenk=0
                break
    elif st[i] == 'S':
        lens=1
        for j in range(i+1,leng):
            if (st[j] == 'T'and st[j-1] == 'R' and st[j-2] == 'A'and st[j-3] == 'T'):
                scnt += 1
                # i=j
                lens=0
                break
    if kcnt < scnt:
        cnt += 1
        kcnt=scnt=0
if cnt > 1:
    n= cnt
    while(n != 1):
        cnt += n-1
        n -= 1
print(cnt)
'''
'''
f= int(input())
a= [0 for i in range(1000)]
while(f != 0):
    b = [int(x) for x in input().split(" ")]
    i = b[0]
    for j in range(2*i):
        if(a[b[j+1]] < 1):
            a[b[j+1]] = 1
    f -= 1
for i in range(1000):
    if(a[i] == 0 and i != 0):
        print(i+1)
        break
'''
import tkinter as tk     # python 3
# import Tkinter as tk   # python 2

class Example(tk.Frame):
    """Illustrate how to drag items on a Tkinter canvas"""

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a canvas
        self.canvas = tk.Canvas(width=400, height=400, background="bisque")
        self.canvas.pack(fill="both", expand=True)

        # this data is used to keep track of an
        # item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        # create a couple of movable objects
        self.create_token(100, 100, "white")
        self.create_token(200, 100, "black")

        # add bindings for clicking, dragging and releasing over
        # any object with the "token" tag
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token", "<B1-Motion>", self.drag)

    def create_token(self, x, y, color):
        """Create a token at the given coordinate in the given color"""
        self.canvas.create_oval(x - 25,y - 25,x + 25,y + 25,outline=color,fill=color,tags=("token",))

    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
'''def f(num):
    sum =0
    while(num >= 0):
        c = num%10
        num /= 10
        f=1
        for i in range(1,c):
            f *= i
        sum += f
    return sum
def sf(num):
    num = f(num)
    sum =0
    while(num >= 0):
        sum += num%10
        num /= 10
    return sum
def g(num):
    n=0
    for i in range(num):
        n = sf(i)
        if(n == num):
            break
    return n
            
def sg(num):
    num = g(num)
    sum =0
    while(num >= 0):
        sum += num%10
        num /= 10
    return sum
'''
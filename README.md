这是一个用回溯算法解数独的程序
### 操作
在格子内左键按下会弹出选择框，选择想填入的数字即可<br>
弹出选择框后，在选择框外左键按下可清除当前格子的数字<br>
（边框属于选择框外的范围，你可以阅读代码看我把数据算的多精致^_^）<br>
按下s键开始回溯，结果将打印在命令提示符中并在屏幕上画出来<br>
按下c键清除所有数字
### 按下s键后
如果填入的数字不合法，会打印wrongful并返回，如行内有2个1，列内有2个1，宫内有2个1等<br>
如果合法将开始回溯，正常的数独只有一种解，可以靠人脑解出来<br>
如果有多种结果，将打印所有结果，但屏幕只会画最后一个解（打印所有结果后）<br>
根据结果的数量，运行需要一定的时间，试试清除所有数字后直接开始回溯会发生什么
### 图形界面
图形化界面的主要难点在数据的计算上，整个图形都是一个个小格子组成的，为了边框粗细一致，每个格子的左边框需要压住左边格子的右边框，上边框需要压住上面格子的下边框<br>
数字的中心和格子的中心需要一致，值得一提的是，画数字需要先将数字转换成图像，但转换后的图像大小并不是刚好包含数字，在底部会有一点点的留白，所以仔细观察程序可以发现数字有一点点的偏上<br>
不同的字体留白的大小还不一样，所以我很难调整，算是一点小瑕疵了<br>
弹出的选择框也是一样的计算，中心和左键按下的位置一致<br>
说的准确一点，选择框不是弹出，而是显示，平时只是隐藏了<br>
计算难度最高的是用点击的位置和选择框点击的位置去操作数组<br>
要知道，所有的位置记录的都是和(0, 0)点的相对距离，元素之间都是独立的！<br>
计算位置让它们看起来是一体的已经很麻烦了，利用记录位置的数据去操作数组内相应的数据更是麻烦<br>
为了完成这个部分，我分别在place和form中创建了2个函数
```
def create_place(self):
    center = self.screen.get_rect().center
    size = self.settings.block_size + self.settings.line_size
    for i in range(9):
        self.place_x.append(center[0] + (i - 4.5) * size + self.settings.line_size // 2 + 1)
        self.place_y.append(center[1] + (i - 4.5) * size + self.settings.line_size // 2 + 1)
```
```
def create_form(self, pos):
    size = self.settings.block_size + self.settings.line_size
    for i in range(3):
        self.form_x.append(pos[0] + (i - 1.5) * size + self.settings.line_size // 2 + 1)
        self.form_y.append(pos[1] + (i - 1.5) * size + self.settings.line_size // 2 + 1)
```
它们记录了每个格子（边框和格子不是一体的）左上角的位置，这样一个长宽为格子大小的正方形就是格子的范围了<br>
这些数组方便了我根据鼠标左键按下时的位置去判断如何操作数组，还很好的避开了边框的位置
```
pos = pygame.mouse.get_pos()
if self.form.flag:
    for i in range(len(self.form.form_x) - 1):
        for j in range(len(self.form.form_y) - 1):
            if (self.form.form_x[i] < pos[0] < self.form.form_x[i] + self.settings.block_size and
                    self.form.form_y[j] < pos[1] < self.form.form_y[j] + self.settings.block_size):
                self.compass.compose[self.form.form_x[-1]][self.form.form_y[-1]] = self.form.sheet[j][i]
                self.form.flag = False
                return
    else:
        self.compass.compose[self.form.form_x[-1]][self.form.form_y[-1]] = ""
        self.form.flag = False
        return
for i in range(len(self.place.place_x)):
    for j in range(len(self.place.place_y)):
        if (self.place.place_x[i] < pos[0] < self.place.place_x[i] + self.settings.block_size and
                self.place.place_y[j] < pos[1] < self.place.place_y[j] + self.settings.block_size):
            self.form.form_x.clear()
            self.form.form_y.clear()
            self.form.create_form(pos)
            self.form.form_x.append(j)
            self.form.form_y.append(i)
            self.form.flag = True
            return
```
整个程序代码量最多的其实是图形界面，用来回溯的代码只有30行左右，但在理解的难易度上远远高于了图形界面
### 回溯原理
首先创建一个检查数字i在当前位置是否合法的函数<br>
行列很好判断，宫内的判断只要观察坐标就可以发现，横坐标整除3结果相等的宫的横坐标也相等，纵坐标同理，别忘了数组都是从0开始的
```
def check(self, row, col, i):
    for m in range(9):
        if self.compose[row][m] == i and m != col or self.compose[m][col] == i and m != row:
            return False
        for n in range(9):
            if m // 3 == row // 3 and n // 3 == col // 3 and self.compose[m][n] == i and m != row and n != col:
                return False
    return True
```
然后就是用来回溯的关键函数了
```
def recall(self, row=0, col=0):
    if col == 9:
        row += 1
        col = 0
        if row == 9:
            self.take.clear()
            for i in range(9):
                self.take.append(list())
                for j in range(9):
                    self.take[i].append(self.compose[i][j])
            print(self.compose)
            return
    if self.compose[row][col] == "":
        for i in range(1, 10):
            if self.check(row, col, i):
                self.compose[row][col] = i
                self.recall(row, col + 1)
        else:
            self.compose[row][col] = ""
    else:
        self.recall(row, col + 1)
```
首先判断横坐标是否超过9（数组索引值为9的是第10个数据），超过就让纵坐标加1并置0，这样就可以遍历整个数组了<br>
当横纵坐标都为9时说明数组已经遍历完了，此时就是一个解了，至于遍历完后我为什么要这样操作，我留着最后讲<br>
然后就是判断当前格子是否需要填数字，如果不需要直接进入下一层<br>
再来看看需要填数字时怎么处理
```
for i in range(1, 10):
    if self.check(row, col, i):
        self.compose[row][col] = i
        self.recall(row, col + 1)
else:
    self.compose[row][col] = ""
```
首先让1到9依次去测试是否合法，如果合法就填上这个数字，然后进入下一层<br>
如果循环完了还没有进入下一层，说明需要开始回溯了<br>
回溯的关键点就在这个循环完了怎么处理上了<br>
如果循环完了不做处理，将直接返回上一层的循环中（仔细思考），这需要在1到9没有一次填入的情况下才能这么处理<br>
一旦填入过一次，不做处理直接返回上一层，这层的值将一直保留，上一层就不会猜测这层的值了，从来让整个回溯出错<br>
循环完了说明1到9都没有合适的数字，不管有没有猜测过，都要把这层的值清除，这就是能回溯的关键了<br>
最后再来讲遍历完后为什么这么处理
```
self.take.clear()
for i in range(9):
    self.take.append(list())
    for j in range(9):
        self.take[i].append(self.compose[i][j])
print(self.compose)
return
```
这很容易理解，就是把数组的值放到take里<br>
理解可变数据类型的特性可能知道，用copy或者[:]的方式不是很快吗，为什么还要用这么麻烦的方式呢<br>
一开始我确实是这么做的，后来发现不管这么修改程序，take的内存地址和compose的内存地址明明不一样，为什么值还是一样的呢<br>
其实这是因为compose是一个二维数组，compose只是一层壳，就算壳的内存地址不一样了，第二层数组的内存地址还是一样的<br>
得到第一个解后还没有结束，将继续回溯求解，一层层往上直到所有都循环完了后置0(前面提到的关键点)才结束<br>
所以compose还是原来的compose，因此要用take记录最后一个解<br>
求解结束后在把take赋值给compose就好了
```
self.compass.compose = self.compass.take.copy()
```
最后在赋值的时候，可以直接使用copy，因为只需要第一层的内存地址不一样，清空take时只是清空了take的内存地址指向，第二层数组不受影响（可变数据类型特性）
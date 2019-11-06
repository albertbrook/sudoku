class Compass(object):
    def __init__(self):
        # self.compose = [["", "", "", 4, "", "", 9, "", ""],
        #                 [4, 3, "", "", 7, "", "", 2, ""],
        #                 [8, "", "", 9, "", 1, 5, 3, ""],
        #                 ["", 6, "", 5, "", "", "", "", ""],
        #                 ["", "", "", "", 1, "", 6, 8, 2],
        #                 [1, "", "", "", "", "", "", "", 3],
        #                 ["", 9, "", 8, "", "", "", 1, 5],
        #                 ["", 1, "", 7, "", "", "", 9, ""],
        #                 ["", "", 2, "", "", "", 7, 4, ""]]
        self.compose = [["", "", 5, 3, "", "", "", "", ""],
                        [8, "", "", "", "", "", "", 2, ""],
                        ["", 7, "", "", 1, "", 5, "", ""],
                        [4, "", "", "", "", 5, 3, "", ""],
                        ["", 1, "", "", 7, "", "", "", 6],
                        ["", "", 3, 2, "", "", "", 8, ""],
                        ["", 6, "", 5, "", "", "", "", 9],
                        ["", "", 4, "", "", "", "", 3, ""],
                        ["", "", "", "", "", 9, 7, "", ""]]
        self.take = list()

    def clear(self):
        self.compose = [[""] * 9 for _ in range(9)]

    def lawful(self):
        for i in range(9):
            for j in range(9):
                if self.compose[i][j] != "" and not self.check(i, j, self.compose[i][j]):
                    return False
        return True

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

    def check(self, row, col, i):
        for m in range(9):
            if self.compose[row][m] == i and m != col or self.compose[m][col] == i and m != row:
                return False
            for n in range(9):
                if m // 3 == row // 3 and n // 3 == col // 3 and self.compose[m][n] == i and m != row and n != col:
                    return False
        return True

# * const
WIDTH = 1000
HEIGHT = 700
BG_color = "#2e2e2e"
board_color = "#035aca"
N = 7
M = 6
Red_turn = True
Yellow_turn = False
token_positions = []
red_won = 3
yellow_won = 2
stale_mate = 1
on_going = 0
for i in range(N):
    token_positions.append(110 + i * 100)


def is_valid_coordinates(i, j):
    return i >= 0 and i < N and j >= 0 and j < M


class slate:
    def __init__(self):
        self.state = on_going
        self.peaks = []
        for i in range(N):
            self.peaks.append(0)
        self.mat = []
        for i in range(N):
            column = []
            for j in range(M):
                column.append(0)
            self.mat.append(column)

    def is_stale(self):
        stale = True
        for i in range(N):
            if self.peaks[i] != M:
                stale = False
        return stale

    def add_token(self, index, turn) -> bool:
        if index<0 or index>=N or self.peaks[index] == M:
            return False
        # - add the token
        self.mat[index][self.peaks[index]] = 1 if turn == Red_turn else -1
        self.peaks[index] += 1
        # - check if the state of the game changed
        scores = [1, 1, 1, 1]
        movenments = [(1, 1), (0, 1), (1, 0), (1, -1)]
        for count, ij in enumerate(movenments):
            i, j = ij
            x, y = index, self.peaks[index] - 1
            while (
                is_valid_coordinates(x + i, y + j)
                and self.mat[x][y] == self.mat[x + i][y + j]
            ):
                scores[count] += 1
                x += i
                y += j
            x, y = index, self.peaks[index] - 1
            while (
                is_valid_coordinates(x - i, y - j)
                and self.mat[x][y] == self.mat[x - i][y - j]
            ):
                scores[count] += 1
                x -= i
                y -= j
        if max(scores) >= 4:
            if turn == Red_turn:
                self.state = red_won
            else:
                self.state = yellow_won
        elif self.is_stale():
            self.state = stale_mate
        return True
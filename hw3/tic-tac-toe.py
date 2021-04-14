import random
import time


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.board = [['n' for _ in range(n)] for _ in range(n)]
        self.ai = AIPlayer()

    def play(self):
        for list in self.board:
            print(list)
        while True:
            # print board
            print('your turn: ')
            vals = input().strip().split(' ')
            print(vals)
            self.place_at((int(vals[0]), int(vals[1])), 'o')
            print('your move: ')
            for list in self.board:
                print(list)
            print()
            if self.is_won():
                break
            # AI's move
            vals = self.ai.pseudo_best(self.board)
            self.place_at((int(vals[0]), int(vals[1])), 'x')
            print('AI\'s move: ')
            for list in self.board:
                print(list)
            print()
            if self.is_won():
                break

    def place_at(self, place: tuple, mark: str) -> bool:
        if place[0] < self.n and place[1] < self.n:
            if self.board[place[0]][place[1]] == 'n':
                self.board[place[0]][place[1]] = mark
                return True
            else:
                print(f'wrong place! {self.board[place[0]][place[1]]} is here.')
                return False

    def is_won(self) -> bool:
        # check 2*n+1 cases
        # in a row
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] != 'n' and self.board[i][0] == self.board[i][j]:
                    count += 1
            if count == 3:
                print(f'{self.board[i][0]} has won!')
                return True
            count = 0
        count = 0
        # in a col
        for j in range(self.n):
            for i in range(self.n):
                if self.board[i][j] != 'n' and self.board[0][j] == self.board[i][j]:
                    count += 1
            if count == 3:
                print(f'{self.board[j][0]} has won!')
                return True
            count = 0
        # others
        count = 0
        for i in range(self.n):
            if self.board[i][i] != 'n' and self.board[0][0] == self.board[i][i]:
                count += 1
            if count == 3:
                print(f'{self.board[0][0]} has won!')
                return True
        count = 0
        for i in range(self.n):
            if self.board[i][self.n - i - 1] != 'n' and self.board[0][self.n - 1] == self.board[i][self.n - i - 1]:
                count += 1
            if count == 3:
                print(f'{self.board[0][self.n - 1]} has won!')
                return True
        return False


class AIPlayer:
    def __init__(self):
        pass

    @staticmethod
    def best_choice(board: list) -> tuple:
        return 0, 0

    @staticmethod
    def pseudo_best(board: list) -> tuple:
        free_list = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'n':
                    free_list.append((i, j))
        select = random.randint(0, len(free_list)-1)
        random.seed(time.time())
        print(free_list[select])
        return free_list[select]


def main():
    game = TicTacToe(3)
    game.play()


if __name__ == '__main__':
    main()

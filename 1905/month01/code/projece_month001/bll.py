"""
    游戏逻辑控制器，负责处理游戏核心算法．
"""

from model import DirectionModel
import random


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [2, 0, 0, 2],
            [4, 4, 2, 2],
            [2, 4, 0, 4],
            [0, 0, 2, 2],
        ]

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾.
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并
        """
        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(self.import01())

    def __move_left(self):
        """
            向左移动
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        """
            向右移动
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __move_up(self):
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    def __move_down(self):
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
            方阵转置
        :param sqr_matrix: 二维列表类型的方阵
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def move(self, dir):
        """
            移动
        :param dir: 方向,DirectionModel类型
        :return:
        """
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()
    def import01(self):
        if random.randint(1,4) == 1:
            return 4
        else:
            return 2


# ---------测试代码---------------
if __name__ == "__main__":
    controller = GameCoreController()
    # controller.move_left()
    # print(controller.map)
    # controller.move_down()
    # print(controller.map)

    # controller.move(DirectionModel.LEFT)
    # print(controller.map)
    controller.move(DirectionModel.RIGHT)
    print(controller.map)
"""
===============
随机漫步次数,随机漫步经过的每个点的 x和 y 坐标
===============

See `~matplotlib.axes.Axes.hexbin`.
"""

from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points=5000):
          """初始化随机漫步的属性"""
          self.num_points = num_points
          # 所有随机漫步都始于(0,0)
          self.x_values = [0]
          self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])




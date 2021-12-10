from django.db import models

# Create your models here.

# 表示用户将要存储的主题的模型
class Topic(models.Model):  #继承了Model——Django中一个定义了模型基本功能的类
    """用户学习的主题"""
    # CharField——由字符或文本组成的数据。存储少量的文本，需告诉Django该在数据库中预留多少空间（200）
    text = models.CharField(max_length=200)
    # DateTimeField——记录日期和时间的数据，auto_add_now=True自动设置成当前日期和时间
    data_added = models.DateTimeField(auto_now_add=True)

    """返回模型的字符串表示"""
    def __str__(self): # 调用方法__str__()来显示模型的简单表示
        return self.text


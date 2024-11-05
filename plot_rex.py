import torch
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 定义绘制混淆矩阵的函数
def plot_confusion_matrix(save_name, y_true, y_pred, classes, normalize=False, title=None, cmap=plt.cm.Blues):
    """
    根据真实标签和预测标签绘制混淆矩阵。

    y_true: 真实标签
    y_pred: 预测标签
    classes: 类别名称列表
    normalize: 是否进行归一化
    title: 图表标题
    cmap: 颜色映射
    """
    if not title:
        if normalize:
            title = 'Normalized Confusion Matrix'
        else:
            title = 'Confusion Matrix'

    # 计算混淆矩阵

    plt.figure(figsize=(50, 50))


    cm = confusion_matrix(y_true, y_pred)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
    disp.plot(cmap=cmap)
    plt.title(title)
    # 保存图像到文件
    plt.savefig(f'{save_name}.png')
    # plt.show()
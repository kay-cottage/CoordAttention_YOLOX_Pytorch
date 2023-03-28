# CoordAttention_YOLOX_Pytorch


*注意：禁止用于商业用途，欢迎个人学习交流！*


## 描述 (Description)

CoordAttention_YOLOX by Pytorch(基于 2021年CVPR CoordAttention坐标注意力机制的改进版YOLOX目标检测平台）

后续可能还会更新：更换backbone主干特征提取网络、添加注意力模块、Attention_YOLOX实际部署等方案



## Paper

* CoordAttention([CVPR2021](https://arxiv.org/abs/2103.02907))



## 环境 (Environment)

* Nvidia Geforce GTX1080Ti
* CUDA10.0
* CUDNN7.0
* windows or linux
* python 3.7


## 注意事项（notes）


1. 改变网络结构后，需要重新训练网络，预训练权重不能用

2. 学习率建议根据自己电脑实际进行设置，小编从0开始重新利用voc数据集训练YOLOX-s网络大概花了几天时间训练了几百个epoch，需要有点耐心呀（首次训练可以考虑使用余弦退火学习率）

3. 小编小小测试，注意力机制放在网络后面的地方似乎更有效（也符合常理），好像也有相关研究支持，当然没有深入研究过


## 预训练权重（Pretrained model）

好久没更了，看到最近有小伙伴让分享下Coodinate Attention YOLOX的预训练权重；由于年代久远只找到这个了，大家可以试一下哈

链接：https://pan.baidu.com/s/1ot5oylilXvLNZnAnQreDPg  提取码：zXip 


## 一些补充（ps）

1. YOLOX 应用在医学领域的血细胞形态学检测中似乎效果也挺好，这里先上个检测的效果图，以后有机会再更新更多例如皮肤癌检测等相关模型

![Imgur](https://mmbiz.qpic.cn/mmbiz_png/QsUWqPChJWaE8j9S6lyjYd87V3BdPROIDgFYjDt09eD7x56KKbcozMOWZVN7A6Aib0lW4ytzf6ztEhgXzba9icNw/0?wx_fmt=png)





## 更多信息：

* 欢迎关注我的bilibili主页：https://space.bilibili.com/362186371

* 更多信息，相关视频会在那里更新

* 最后，该项目为个人想法的简单实现，敬请期待，以后想到idea再更！

* 不喜勿喷，谢谢哈


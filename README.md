# trace

此项目用于做一个读取配置文件并用配置文件内容控制流操作的练习
xml文件是一个控制轨迹走动的点
beginspot标签用于定义起始点横纵轴坐标（x,y）
step标签用于说明每一步行走的方向，一共有8种方向：
up：            上
down：          下
left：          左
right：         右
leftup：        左上
leftdown：      左下
rightup：       右上
rightdown：     右下


初步计划，行走于一个3000*3000的正方形上，如果超过这个正方形就会撞墙（hitwall）
最后运行之后，把配置文件所描述的轨迹画出一张图。
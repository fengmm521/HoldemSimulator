# HoldemSimulator

德州扑克算法模拟器

德州扑克（Texas hold'em，有时也简称为Hold'em或Holdem），简称德扑

## 扑克牌序列生成方案

假如有9个人一起玩，9个人分别定义为p1,p2,p3,p4,p5,p6,p7,p8,p9这也是德扑的最大玩家数量

1.玩家首先需要把自已的帐户在区块链上的状态更改为加入德扑游戏的锁定帐户，当帐户人数达到2人以上时，玩家可以开始游戏，每次游戏开始都要所有的的玩家签名才可以开局，以防止有玩家同时进入多局游戏中

2.每个玩家生成一个RSA的公私钥密钥对，用于本局游戏。分别为p1Pub,p1Pri...等等

3.将所有的9个公钥收集起来按数值从小到大排列。定义为玩家的坐位编号,同时每个玩家使用自已的帐户私钥对这个起始编号和生成的9个公钥，以及9个帐户地址的数据打包并签名

4.将排列好的9个公钥连接在一起，送入sha512得到一个hash输出。然后对这个输出作为字节数组输出

4.对这个输出取52的余数，得到不重复的1～52的一组随机序列，如果一次取得的余数有重复使得到的序列不够52个，则对公钥生成的sha521结果再次取sha512,一直重复，直到得到52个值的序列，先定义这个序列为list0

6.每个玩家使用自已的私钥送入sha512得到一个hash输出，然后使用与3到5同样的方法，分别得到各自的52个不同数值的序列，定义9个玩家的序列分别的，list1~list9

## 发牌方案

1.首先所有人使用自已的list列表对其他玩家发底牌，发牌方案如下

    1)按p1~p9的顺序，各个玩家使用自已的list中的第一个和第二个分别对list0的不同玩家手牌朝晖 行解析，但每个玩家自已保留自已对自已的解析值
    2）因为自已手牌需要由自已list解析的结果确定的，所以只有自已知道自已的底牌是什么

2.所有玩家得到开始的两张底牌后，开始初始下注

3.开始发桌面的三张底牌，方案如下

    因为桌面上最开始的三张牌是大家都可以看到的牌，所以p1~p9所有人都使用自已对应编号的数值对list0中的对应三个位置的牌解析，可以得到桌面的三张牌是什么

4.以此类推，所有的扑克其实是由所有玩家的list和发牌时的list0控制，每个玩家都控制着所有的公共牌值，同时也控制着自已的手牌

5.每一次对扑克解析时，都使用上一次解析的sha256加这次的解析结果作一个sha256运算，下一次又使用当前的sha256值作为下一次的输入，这样将整个开牌顺序制作成一个sah256链，使一局游戏成为一个整体

6.当一局结束后，可由任何一个玩家将本局游戏结果发送到区块链上以分配各自的输赢结果


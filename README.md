<div align="center">

# Yap
Yet Another Genshin Impact Pickupper

又一个原神拾取器

_Named from [Yas](https://github.com/wormtql/yas)_

</div>

# 介绍

借鉴了[Yas](https://github.com/wormtql/yas)代码实现的自动拾取器。

一个跑的飞快、占用资源低、可配置黑名单的自动拾取器，解放玩家的F键。


除了版本更新检测外，已基本完工。（可能也不会考虑去做另一个基于图像分类的方案了）

- [x] 1. 模型训练
- [x] 2. 模型转换
- [x] 4. F key 寻找
- [x] 10. F key Find api
- [ ] 5. version update detection
- [x] 6. Capture
- [x] 7. image Preprocess
- [x] 3. 模型部署及测试
- [x] 8. F key press
- [x] 9. Scroll press

# 使用

## 1. 获取可执行文件

下载 or 编译得到可执行文件

编译使用
```
cargo build --release
```

## 2. 配置F key图像

需要复制项目中的`models/FFF.bmp`（见下图）至可执行文件同目录下。

![f key image](./models/FFF.bmp)

注：图像大小目前在代码中是硬编码的，更改后应该会报错


## 3. 配置黑名单

需要复制项目中的`models/black_lists.json`（见下图）至可执行文件同目录下。


将需要拉黑的拾取物品名称添加至`black_lists.json`中，如下所示。
```json
[
    "史莱姆凝液",
    "污秽的面具",
    "破损的面具",
]
```

## 4. 运行

Enjoy it!

就是目前模型还处于不太认识字的情况233，基本只认识蒙德区域的拾取物品。

目前会默认将可能是文字的图片保存，所以需要指定一个起始的idx，后面再改了。

```bash
./yap.exe 0
```


# 优劣

## 优点
1. 跑的快，单次推理速度低于10ms
2. 不占用GPU，使用CPU推理
3. 可执行文件体积小，加上CRNN模型仅14+MB
4. 更低的内存占用（对比各种python实现）
5. **开箱即用**，无需等待配置环境时的pip及github下载。
6. 专注于拾取，配置黑名单，锄地玩家解放F键

## 缺点
1. 编译速度太tmd慢了
2. 模型目前精度不佳，训练时使用了一半真实数据一半生成数据
3. 目前仅支持16:9的分辨率
4. 拾取逻辑默认往下滚动，带来冗余
5. 跑的太快，两次检测之间硬编码了一个100ms的延迟
6. 因为使用中文识别，所以添加新词还需要改网络架构重新训练
7. F键寻找的算法（模板匹配）在灰度通道精度太低，需要尝试其他通道


相比拥有黑名单的自动拾取，如隔壁的[GIA](https://github.com/infstellar/genshin_impact_assistant)。rust带来了**更快**的运行速度（单次推理速度低于10ms vs 至少比10ms慢），**更小**的体积（14+MB vs 若干个GB），**更低**的内存占用（显然）。但是在模型精度方面还需要更多的“人工”智biao能zhu。
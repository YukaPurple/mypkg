![test](https://github.com/YukaPurple/robosys2022/actions/workflows/test.yml/badge.svg)

# mypkg
このリポジトリは千葉工業大学ロボットシステム学の講義で作成したROS2のパッケージである。

talkerとlistenerという2つのノードが通信するのを確認することができる。


# 機能
## talker
0.5秒おきにメッセージを送信する。

メッセージの自然数が1ずつ増えていく。

- 実行方法

```
$ ros2 run mypkg talker
```

## listener
tallerからのメッセージを受け取り、メッセージを画面に表示する。

tallerとlistenerはそれぞれ別の端末で実行する必要がある。


- 実行方法

```
$ ros2 run mypkg listener
```

# launchファイル
このファイルを使用することで、talkerとlistenerを同時に実行することができる。

- 実行方法

```
$ ros2 launch mypkg talk_listen.launch.py
```


# テスト環境
- Ubuntu 22.04

# ソフトウェア
- Python3.10

# ライセンス

- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

- © 2023 Yukari Watarai


# Remote Procedure Call

## 概要
　ネットワークの学習の一環で，プロセス間通信を用いたリモートプロシージャコールの実装をしました．<br>
　クライアント(JavaScript)から，UNIXドメインソケットを用いてJSON形式のデータをサーバー(Python)へ送ります．受け取ったデータをもとに関数を実行して，結果をJSON形式にしてクライアントへ送り返します．

## 使用技術
<img src="https://img.shields.io/badge/-Ubuntu-ffffff.svg?logo=ubuntu&style=popout">
<img src="https://img.shields.io/badge/-Python-ffff00.svg?logo=python&style=popout">
<img src="https://img.shields.io/badge/-JavaScript-006ab6.svg?logo=javascript&style=popout">

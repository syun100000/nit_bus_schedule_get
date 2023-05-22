
# NIT バススケジュールアプリ

このアプリケーションは、NIT（某大学）のバスのスケジュールを表示するためのWebアプリケーションです。

## 概要

このアプリケーションは、Flaskフレームワークを使用して構築されています。バスのスケジュール情報は、https://www.nit.ac.jp/campus/access/bus-schedule からスクレイピングして取得します。以下の路線の次のバスの出発時刻を表示します:

- 新白岡駅→大学
- 大学→新白岡駅
- 東武動物公園駅→大学
- 大学→東武動物公園駅

## インストール

1. このリポジトリをクローンします:

   ```
   git clone https://github.com/your/repository.git
   ```

2. 必要なパッケージをインストールします:

   ```
   pip install -r requirements.txt
   ```

3. アプリケーションを実行します:

   ```
   python app.py
   ```

4. ブラウザで `http://localhost:5000` を開きます。

## 使用法

- トップページには各路線の次のバスの出発時刻が表示されます。
- ページは定期的に自動的に更新され、最新のバスの情報が表示されます。

## 技術的詳細

- Python 3を使用しています。
- Flaskフレームワークを使用してWebアプリケーションを構築しています。
- BeautifulSoupを使用してウェブサイトからバスのスケジュールをスクレイピングしています。

## 注意事項

- バスの運行状況はリアルタイムではなく、事前にスケジュールされた情報です。
- 表示される出発時刻は参考のため、実際の出発時刻とは異なる場合があります。

以上が、バススケジュールアプリのREADME.mdの例です。ご参考までにどうぞ。

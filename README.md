# ArgkExplorer

新垣結衣さんの様々な情報を発信するTwitter Bot開発用リポジトリ

## 環境

* [ConoHa WING]( https://www.conoha.jp/wing/) で立ち上げた CloudLinux 上で動作することを前提として開発
* 連携先ツイッターアカウント : https://twitter.com/yui_media_info

## モジュール一覧

役割ごとにモジュール化し、各モジュールはcronによって実行周期を制御する

* Get系
    * GetSearchTW
        * キーワード検索によってツイートを取得する
    * GetUserRT
        * 特定ユーザのRTを取得する
    * GetUserFV
        * 特定ユーザのいいねを取得する
* Post系
    * PostRT
        * RTすべきと判断したツイートをRTする
    * PostWebInfo
        * Webサイトの更新情報をツイートする
    * PostMagazineInfo
        * 雑誌情報をツイートする
    * PostAnniversary
        * 記念日をツイートする
    * PostScreenName
        * スクリーンネームを変更する
* LearnHomeTL
    * RTすべきツイートを学習する
* CategorizeTW
    * ツイートをカテゴライズする

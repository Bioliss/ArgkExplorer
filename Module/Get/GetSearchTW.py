#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""キーワード検索によってツイートを取得する

DBに登録された新垣結衣さんに関する様々なキーワードでツイートを検索する
検索した結果をDBに登録する
"""
def read_config(bl_test_flg: bool) -> bool:
"""json形式の設定ファイルを読み込み

Twitter API や DB へアクセスするためのアカウント情報が記載されたjson形式の設定ファイルを読み込む

Arguments:
    bl_test_flg {bool} -- テスト用アカウント使用時 : True

Returns:
    bool -- 成功 : True / 失敗 : False
"""

def gen_query(list_keyword: list) -> list:
"""検索クエリの生成
一度に複数キーワードで検索するための処理

Arguments:
    list_keyword {list} -- DBから取得したキーワードのリスト

Returns:
    list -- 検索文字列のリスト
"""

def parse_created_at(str_created_at: str) -> str:
"""created_atをYYYY-MM-DD HH:MM:SS形式に変換

Arguments:
    str_created_at {str} -- Twitter APIで取得した created_at

Returns:
    str -- DB用に整形した created_at
"""

def get_search_tweets(str_query: str) -> list:
"""ツイートを取得する

Arguments:
    str_query {str} -- 検索文字列

Returns:
    list -- Twitter APIの応答データ
"""

def set_tweet_info(status: list) -> bool:
"""ツイート情報をDBに登録する

Arguments:
    status {list} -- Twitter APIの応答データ

Returns:
    bool -- DBへの登録成功 : True / 失敗 : False
"""

def set_user_info(status: list) -> bool:
"""ツイートユーザ情報をDBに登録する

Arguments:
    status {list} -- Twitter APIの応答データ

Returns:
    bool -- DBへの登録成功 : True / 失敗 : False
"""    
# created_at の変換処理

def main():
    # json形式の設定ファイルを読み込み
    if read_config(False) == False:
        print("json形式の設定ファイル読み込みに失敗しました")
        return

    for list_status in get_search_tweets(gen_query()):
        if set_tweet_info(list_status) == False:
            continue
        if set_user_info(list_status) == False:
            continue

if __name__ == '__main__':
    main()
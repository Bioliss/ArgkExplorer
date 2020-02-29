#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""キーワード検索によってツイートを取得する

DBに登録された新垣結衣さんに関する様々なキーワードでツイートを検索する
検索した結果をDBに登録する
"""

import GetCommon

def gen_query() -> list:
    """検索クエリの生成
    一度に複数キーワードで検索するための処理

    Returns:
        list -- 検索文字列のリスト
    """

def get_search_tweets(str_query: str) -> list:
    """ツイートを取得する

    Arguments:
        str_query {str} -- 検索文字列

    Returns:
        list -- Twitter APIの応答データ
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
    if GetCommon.read_config(False) == False:
        print("json形式の設定ファイル読み込みに失敗しました")
        return

    for list_status in get_search_tweets(gen_query()):
        if GetCommon.set_tweet_info(list_status) == False:
            continue
        if set_user_info(list_status) == False:
            continue

if __name__ == '__main__':
    main()
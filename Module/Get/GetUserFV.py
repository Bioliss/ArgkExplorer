#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""特定ユーザのいいねを取得する

新垣結衣さんのファン(ガキラーさん)ユーザのいいねを取得しDBに登録する
"""
import GetCommon

def get_gakilar_id_from_db() -> list:
    """ガキラーさんリストの取得
    DBに登録されたユーザ情報の内ガキラーさんのユーザ情報を抽出

    Returns:
        list -- Twitter ユーザID
    """

def get_gakilar_fav(str_gakilar_id: str) -> list:
    """ガキラーさんがいいねしたツイートを取得

    Arguments:
        str_gakilar_id {str} -- ガキラーさんのユーザID

    Returns:
        list -- ガキラーさんがいいねしたツイート
    """    
    
def main():
    # json形式の設定ファイルを読み込み
    if GetCommon.read_config(False) == False:
        print("json形式の設定ファイル読み込みに失敗しました")
        return

    for str_galilar_id in get_gakilar_id_from_db():
        for list_status in get_gakilar_fav(str_galilar_id):
            if GetCommon.set_tweet_info(list_status) == False:
                continue

if __name__ == '__main__':
    main()
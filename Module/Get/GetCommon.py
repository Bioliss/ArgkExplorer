#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""共通処理

各モジュールからの呼び出しを想定した共通処理
"""

def read_config(bl_test_flg: bool) -> bool:
    """json形式の設定ファイルを読み込み

    Twitter API や DB へアクセスするためのアカウント情報が記載されたjson形式の設定ファイルを読み込む

    Arguments:
        bl_test_flg {bool} -- テスト用アカウント使用時 : True

    Returns:
        bool -- 成功 : True / 失敗 : False
    """

def parse_created_at(str_created_at: str) -> str:
    """created_atをYYYY-MM-DD HH:MM:SS形式に変換

    Arguments:
        str_created_at {str} -- Twitter APIで取得した created_at

    Returns:
        str -- DB用に整形した created_at
    """

def set_tweet_info(status: list) -> bool:
    """ツイート情報をDBに登録する

    Arguments:
        status {list} -- Twitter APIの応答データ

    Returns:
        bool -- DBへの登録成功 : True / 失敗 : False
    """

def get_gakilar_id_from_db() -> list:
    """ガキラーさんリストの取得
    DBに登録されたユーザ情報の内ガキラーさんのユーザ情報を抽出

    Returns:
        list -- Twitter ユーザID
    """

def main():
    print('このスクリプトは、他のモジュールから呼び出す想定のスクリプトです。')

if __name__ == '__main__':
    main()

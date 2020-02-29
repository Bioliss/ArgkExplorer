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

def main():
    print('このスクリプトは、他のモジュールから呼び出す想定のスクリプトです。')

if __name__ == '__main__':
    main()

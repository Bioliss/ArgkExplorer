#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""スクリーンネームを変更する

金曜日には「金曜日の新垣さん」、土曜日には「土曜日の新垣さん」のように
スクリプト実行時の曜日に応じてスクリーンネームを変更する
"""
import PostCommon

def get_week() -> int:
    """スクリプト実行時の曜日を取得

    Returns:
        int -- 曜日のインデックス値
    """    

def gen_name(int_week_index: int) -> str:
    """スクリーンネームの生成

    Arguments:
        int_week_index {int} -- 曜日のインデックス値

    Returns:
        str -- スクリーンネーム
    """    

def post_name(str_week: str) -> bool:
    """スクリーンネームの更新

    Arguments:
        str_week {str} -- スクリーンネーム

    Returns:
        bool -- 更新成功 : True / 失敗 : False
    """

def post_icon(int_week_index: int) -> bool:
    """アイコンの変更

    Arguments:
        int_week_index {int} -- 曜日のインデックス値

    Returns:
        bool -- 更新成功 : True / 失敗 : False
    """    

def post_header(int_week_index: int) -> bool:
    """ヘッダーの変更

    Arguments:
        int_week_index {int} --  曜日のインデックス値

    Returns:
        bool -- 更新成功 : True / 失敗 : False
    """    

def main():
    # json形式の設定ファイルを読み込み
    if PostCommon.read_config(False) == False:
        print("json形式の設定ファイル読み込みに失敗しました")
        return
    int_week_index = get_week()
    if post_name(gen_name(int_week_index)) == False:
        print("スクリーンネームの変更に失敗しました")
        return
    if post_icon(int_week_index) == False:
        print("アイコンの変更に失敗しました")
        return
    if post_header(int_week_index) == False:
        print("ヘッダーの変更に失敗しました") 
        return

if __name__ == '__main__':
    main()
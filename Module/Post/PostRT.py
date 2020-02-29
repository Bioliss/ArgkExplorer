#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""RTすべきと判断したツイートをRTする

AnalyzeモジュールによってRTすべきと判断されたツイートをRTする
"""
import PostCommon

def get_tweet_id_from_db() -> list:
    """RT対象ツイートIDの取得
    DBに登録されたツイート情報の内RTすべきと判断されたツイートを抽出

    Returns:
        list -- ツイートID
    """

def post_rt(str_tweet_id: str) -> str:
    """RTすべきと判断されたツイートをRT

    Arguments:
        str_tweet_id {str} -- RTすべきと判断されたツイートID

    Returns:
        str -- RTのツイートID
    """    

def set_rt_log_to_db(str_tweet_id: str, str_rt_id: str) -> bool:
    """RTログをDBに登録
    RTのツイートIDをDBに登録

    Arguments:
        str_tweet_id {str} -- ツイートID
        str_rt_id {str} -- RTID

    Returns:
        bool -- DBへ登録成功 : True / 失敗 : False
    """    

def main():
    # json形式の設定ファイルを読み込み
    if PostCommon.read_config(False) == False:
        print("json形式の設定ファイル読み込みに失敗しました")
        return

    for str_tweet_id in get_tweet_id_from_db():
        if set_rt_log_to_db(str_tweet_id, post_rt(str_tweet_id)) == False:
            continue

if __name__ == '__main__':
    main()
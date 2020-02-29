#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""RTすべきツイートを学習するための情報をDBに登録する

DBに記録されたRT済みツイートがHomeTLから削除されていた場合、RTすべきでなかったツイートである旨DBに登録する
DBに記録されていないツイートがHomeTLに存在した場合、RTすべきツイートである旨DBに登録する
"""
import AnalyzeCommon

def get_rt_id_from_db() -> list:
    """RT済みツイートIDのチェック

    DBに記録されたRT済みツイートIDを検索し、すべてのツイートIDを返す

    Returns:
        list -- ツイートID
    """    

def chk_rt_id_from_db(str_rt_id: str) -> bool:
    """DBに記録されたRT済みツイートとHomeTLを比較

    DBに記録されたRT済みツイートIDでTwitter APIを用いて検索し
    検索結果に応じてHomeTLから意図的に削除されたかを判断する

    Arguments:
        str_rt_id {str} -- 検索対象のツイートID

    Returns:
        bool -- 意図的に削除されていない : True / 意図的に削除された : False
    """    

def get_rt_id_from_tl() -> list:
    """Home TLの取得
    Twitter APIを用いてHome TLを取得し、取得したすべてのツイートIDを返す

    Returns:
        list -- ツイートID
    """

def chk_rt_id_from_tl(str_rt_id: str) -> bool:
    """TLにあるツイートがDBに登録済みか調べる

    Arguments:
        str_rt_id {str} -- 検索対象のツイートID

    Returns:
        bool -- 登録済み : True / 未登録 : False
    """

def set_un_needed(str_rt_id: str) -> bool:
    """RTすべきでなかったツイートである旨DBに登録する

    Arguments:
        str_rt_id {str} -- 登録対象のツイートID

    Returns:
        bool -- DB更新成功 : True / DB更新失敗 : False
    """

def set_needed(list_rt_info: list) -> bool:
    """RTすべきツイートである旨DBに登録する

    Arguments:
        list_rt_info {list} -- 登録対象のツイート情報

    Returns:
        bool -- DB更新成功 : True / DB更新失敗 : False
    """

def main():
    # json形式の設定ファイルを読み込み
    if AnalyzeCommon.read_config(False) == False:
        print("json形式の設定ファイル読み込みに失敗しました")
        return

    # RTすべきでなかったツイートの登録
    for str_rt_info in get_rt_id_from_db():
        if chk_rt_id_from_db(str_rt_info["id_str"] ) == True:
            continue
        if set_un_needed(str_rt_info["id_str"] ) == False:
            print("失敗 : set_un_needed()")

    # RTすべきツイートの登録
    for str_rt_info in get_rt_id_from_tl():
        if chk_rt_id_from_tl(str_rt_info["id_str"]) == True:
            continue
        if set_needed(str_rt_info) == False:
            print("失敗 : set_needed()")

if __name__ == '__main__':
    main()
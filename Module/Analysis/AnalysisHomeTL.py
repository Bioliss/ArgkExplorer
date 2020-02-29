#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""RTすべきツイートを学習するための情報をDBに登録する

DBに記録されたRT済みツイートがHomeTLから削除されていた場合、RTすべきでなかったツイートである旨DBに登録する
DBに記録されていないツイートがHomeTLに存在した場合、RTすべきツイートである旨DBに登録する
"""

def ReadConfig(blTestFlg: bool) -> bool:
"""json形式の設定ファイルを読み込み

Twitter API や DB へアクセスするためのアカウント情報が記載されたjson形式の設定ファイルを読み込む

Arguments:
    blTestFlg {bool} -- テスト用アカウント使用時 : True

Returns:
    bool -- 成功 : True / 失敗 : False
"""


def GetRTIDFromDB() -> list:
"""RT済みツイートIDのチェック

DBに記録されたRT済みツイートIDを検索し、すべてのツイートIDを返す

Returns:
    list -- ツイートID
"""    

def ChkRTIDFromDB(sRTID: str) -> bool:
"""DBに記録されたRT済みツイートとHomeTLを比較

DBに記録されたRT済みツイートIDでTwitter APIを用いて検索し
検索結果に応じてHomeTLから意図的に削除されたかを判断する

Arguments:
    sRTID {str} -- 検索対象のツイートID

Returns:
    bool -- 意図的に削除されていない : True / 意図的に削除された : False
"""    

def GetTWIDFromTL() -> list:
"""Home TLの取得
Twitter APIを用いてHome TLを取得し、取得したすべてのツイートIDを返す

Returns:
    list -- ツイートID
"""

def ChkRTIDFromTL(sRTID: str) -> bool:
"""TLにあるツイートがDBに登録済みか調べる

Arguments:
    sRTID {str} -- 検索対象のツイートID

Returns:
    bool -- 登録済み : True / 未登録 : False
"""

def SetUnNeeded(sRTID: str) -> bool:
"""RTすべきでなかったツイートである旨DBに登録する

Arguments:
    sRTID {str} -- 登録対象のツイートID

Returns:
    bool -- DB更新成功 : True / DB更新失敗 : False
"""

def SetNeeded(sRTInfo: list) -> bool:
"""RTすべきツイートである旨DBに登録する

Arguments:
    sRTID {list} -- 登録対象のツイート情報

Returns:
    bool -- DB更新成功 : True / DB更新失敗 : False
"""

def main():
    # json形式の設定ファイルを読み込み
    if ReadConfig(False) == False:
        print("json形式の設定ファイル読み込みに失敗しました")
        return

    # RTすべきでなかったツイートの登録
    for sRTInfo in GetRTIDFromDB()
        if ChkRTIDFromDB(sRTInfo["id_str"] ) == True:
            continue
        if SetUnNeeded(sRTInfo["id_str"] ) == False:
            print("失敗 : SetUnNeeded()")

    # RTすべきツイートの登録
    for sRTInfo in GetTWIDFromTL()
        if ChkRTIDFromTL(sRTInfo["id_str"]) == True:
            continue
        if SetNeeded(sRTInfo) == False:
            print("失敗 : SetNeeded()")

if __name__ == '__main__':
    main()
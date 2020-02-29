#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""ツイート情報の解析

DBに記録されたツイート情報をもとに、
RTすべきでないツイートとRTすべきツイートを分類するためのfastText用モデルデータを作成する
"""

def read_config(bl_test_flg: bool) -> bool:
"""json形式の設定ファイルを読み込み

Twitter API や DB へアクセスするためのアカウント情報が記載されたjson形式の設定ファイルを読み込む

Arguments:
    bl_test_flg {bool} -- テスト用アカウント使用時 : True

Returns:
    bool -- 成功 : True / 失敗 : False
"""

def get_tw_from_db(str_db_field : str) -> list:
  """DBからツイートを取得
  
  Arguments:
      str_db_field {string} -- RTすべきでないツイートとRTすべきツイートの識別子
  
  Returns:
      list -- SQLの応答データ
  """
  cursor.execute(str_sql)
  return cursor.fetchall()

def get_surfaces(list_sql_ret :list) -> list:
  """ツイートを分かち書きし単語単位に分割
  
  Arguments:
      list_sql_ret {list} -- DBから取得したツイート情報
  
  Returns:
      list -- 分かち書きされたツイート文
  """
  list_results = []
  for list_sql_record in list_sql_ret:
    str_tweet = list_sql_record[0]
    str_tweet = format_text(str_tweet)
    tagger = MeCab.Tagger('')
    tagger.parse('')

    list_surf = []
    node = tagger.parseToNode(str_tweet)
    while node:
      surf.append(node.surface)
      node = node.next
      
    list_results.append(list_surf)
  return list_results

def write_txt(list_tweet :list, str_db_field :str, obj_file :object):
    """評価モデル用のテキストファイル作成
    
    Arguments:
        list_tweet {list} -- 分かち書きされたツイート文
        target {int} -- RTすべきでないツイートとRTすべきツイートの識別子
        obj_file {object} -- 評価モデル用のテキストファイル
    """        
    try:
        if(len(list_tweet) > 0):
        str_label = "__label__" + str_db_field + ", "
        for str_tweet in list_tweet:
            # 文字列がほぼなしの場合はSkip
            if( len(row) < 3 ):
            continue
            # 空行区切りの文字列に変換
            str_space_separate = " ".join(str_tweet)
            str_line_text = str_label + str_space_separate + "\n"
            # 書き込み
            obj_file.write(str_line_text.decode('UTF-8'))

        print(str(len(list_tweet))+"行を書き込み")

    except Exception as e:
        print("テキストへの書き込みに失敗")
        print(e)

def format_text(text :str) -> str:
    """ツイートから不要な文字列を除去
    
    Arguments:
        text {str} -- ツイート文
    
    Returns:
        str -- 不要な文字列を除去したツイート文
    """
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', " ", text)
    text=re.sub(r'@[\w/:%#\$&\?\(\)~\.=\+\-…]+', " ", text)
    text=re.sub(r'&[\w/:%#\$&\?\(\)~\.=\+\-…]+', " ", text)
    text=re.sub(u'[^ぁ-んァ-ヶーa-zA-Z0-9一-龠０-９]', " ", text)
    text=re.sub(';', " ", text)
    text=re.sub('RT', " ", text)
    text=re.sub('\n', " ", text)
    text=re.sub('   ', " ", text)
    text=re.sub('  ', " ", text)
    return text.encode('UTF-8', 'ignore')

def main():
    LIST_DB_FIELD = ["yNeeded", "yUnneed"]
    STR_FILE_NAME = "model.txt"
    obj_file = codecs.open(STR_FILE_NAME, 'w', 'utf-8')
    read_config()

    for str_db_field in LIST_DB_FIELD:
        list_sql_ret = get_tw_from_db(str_db_field)       #ツイートを取得
        list_surfaces = get_surfaces(list_sql_ret)        #ツイートを分かち書き
        write_txt(list_surfaces, str_db_field, obj_file)  #ツイートを書き込み

    obj_file.close()
    ft.supervised(STR_FILE_NAME, "model")                 #model.binを作成

if __name__ == '__main__':
    main()

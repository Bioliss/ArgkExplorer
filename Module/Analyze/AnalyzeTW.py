#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""ツイート情報の解析

DBに記録されたツイート情報をもとに、
RTすべきでないツイートとRTすべきツイートを分類するためのfastText用モデルデータを作成する
"""

def ReadConfig(blTestFlg: bool) -> bool:
"""json形式の設定ファイルを読み込み

Twitter API や DB へアクセスするためのアカウント情報が記載されたjson形式の設定ファイルを読み込む

Arguments:
    blTestFlg {bool} -- テスト用アカウント使用時 : True

Returns:
    bool -- 成功 : True / 失敗 : False
"""

def get_tweet(target):
  '''
  tweetLogTBLからツイート取得
  '''
  sqlText = 'SELECT textFull from `tweetLogTBL` WHERE ' + target + ' > 80'
  cursor.execute(sqlText)
  return cursor.fetchall()

def get_surfaces(contents):
  '''
  文書を分かち書きし単語単位に分割
  '''
  results = []
  for i in contents:
    row = i[0]
    content = format_text(row)
    tagger = MeCab.Tagger('')
    tagger.parse('')
    surf = []
    node = tagger.parseToNode(content)
    while node:
      surf.append(node.surface)
      node = node.next
    results.append(surf)
  return results

def write_txt(contents, target, f):
    '''
    評価モデル用のテキストファイルを作成する
    '''
    try:
        if(len(contents) > 0):
        labelText = "__label__" + str(target) + ", "
        for row in contents:
            # 文字列がほぼなしの場合はSkip
            if( len(row) < 3 ):
            continue
            # 空行区切りの文字列に変換
            spaceTokens = " ".join(row);
            result = labelText + spaceTokens + "\n"
            # 書き込み
            f.write(result.decode('UTF-8'))

        print(str(len(contents))+"行を書き込み")

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
    targetList = ["yNeeded", "yUnneed"]
    fileName = "model.txt"
    f = codecs.open(fileName, 'w', 'utf-8')
    ReadConfig()

    for target in range(len(targetList)):
        sqlret = get_tweet(targetList[target]) #ツイートを取得
        surfaces = get_surfaces(sqlret)        #ツイートを分かち書き
        write_txt(surfaces, target, f)         #ツイートを書き込み

    f.close()

    classifier = ft.supervised(fileNema, "model")   #model.binを作成

if __name__ == '__main__':
    main()


from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 揣釋義
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 加文字
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 揣文字上大流水號
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 加關係
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 用主碼號揣流水號
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 袂當替換
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 義近
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 揣關係上大流水號
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 用釋義揣例句
from 教育部臺灣閩南語常用詞辭典.造字處理 import 共造字換做統一碼表示法
from 教育部臺灣閩南語常用詞辭典.造字處理 import 解析器
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 設定編修狀況
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 設定文字組合
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 用流水號揣腔口
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 國語臺員腔
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 設定無音文字

for 釋義編號, 主編號, 詞性, 釋義 in 揣釋義():
    加文字('語句', 國語臺員腔, 釋義, '')
    釋義流水號 = 揣文字上大流水號()
    例句資料 = 用釋義揣例句(釋義編號)
    臺語流水號集 = 用主碼號揣流水號(主編號)
    for 例句, 標音, 例句翻譯 in 例句資料:
        加文字('語句', 國語臺員腔, 例句翻譯, '')
        國語例句流水號 = 揣文字上大流水號()
        for 臺語流水號 in 臺語流水號集:
            加關係(臺語流水號[0], 釋義流水號, 義近, 袂當替換)
            解釋關係流水號 = 揣關係上大流水號()
            for 例句, 標音, 例句翻譯 in 例句資料:
                if 標音[0].isupper():
                    種類 = '語句'
                else:
                    種類 = '字詞'
                解析結果, 合法無 = 解析器.解析語句佮顯示毋著字元(標音)
                if 合法無:
                    上傳音標 = 解析結果
                else:
                    上傳音標 = 標音
                臺語腔口 = 用流水號揣腔口(臺語流水號[0])
                加文字(種類, 臺語腔口, 共造字換做統一碼表示法(例句), 上傳音標)
                例句流水號 = 揣文字上大流水號()
                if 合法無:
                    設定編修狀況(例句流水號, '正常')
                else:
                    設定編修狀況(例句流水號, '音標有問題')
                設定文字組合(國語例句流水號, ',' + str(解釋關係流水號) + ',')
設定無音文字()

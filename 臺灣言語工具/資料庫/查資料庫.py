"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.資料庫.資料庫連線 import 資料庫連線
from 臺灣言語工具.字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.字詞組集句章.解析整理工具.文章粗胚工具 import 文章粗胚工具
from 臺灣言語工具.資料庫.欄位資訊 import 閩南語

class 查資料庫:
	粗胚工具=文章粗胚工具()
	分析器=拆文分析器()
	家私=轉物件音家私()
	
	查型體翻譯著=資料庫連線.prepare('SELECT DISTINCT' +
			'"寅"."型體","寅"."音標" ' +
			'FROM "言語"."文字" AS "子", "言語"."關係" AS "丑", "言語"."文字" AS "寅" ' +
			' WHERE "子"."腔口"=$1 AND "子"."型體"=$2 AND ' +
			'"丑"."甲流水號"="子"."流水號" AND "丑"."乙流水號"="寅"."流水號" AND "丑"."乙對甲的關係類型"=\'義近\' AND ' +
			'"寅"."腔口"=$3 '
			#'ORDER BY "寅"."流水號"'
			)
	揣台華型體 = 資料庫連線.prepare('SELECT ' +
		' "台語漢字","台語羅馬字" '
		'FROM "楊允言先生資料"."台華" ' +
		' WHERE "華語對譯" LIKE $1 '+
		'ORDER BY "ID"')
	
# 	揣詞六型體 = lambda 原來腔口, 型態:資料庫連線.prepare('SELECT ' +
# 		' "台語漢字","台語音標" '
# 		'FROM "整理中的台語詞典"."整理中的台語詞典06" ' +
# 		'WHERE "華語漢字"=$1 '+
# 				'ORDER BY "識別碼"')('%;'+型態+';%')
	def 型體翻譯著(self,原來腔口, 型態, 欲揣腔口):
# 		結果=資料庫連線.prepare('SELECT ' +
# 			'"寅"."流水號","寅"."來源","寅"."種類","寅"."腔口","寅"."地區","寅"."年代",'+
# 			'"寅"."組合","寅"."型體","寅"."音標","寅"."調變","寅"."音變" ' +
# 			'FROM "言語"."文字" AS "子", "言語"."關係" AS "丑", "言語"."文字" AS "寅" ' +
# 			' WHERE "子"."腔口"=$1 AND "子"."型體"=$2 AND ' +
# 			'"丑"."甲流水號"="子"."流水號" AND "丑"."乙流水號"="寅"."流水號" AND "丑"."乙對甲的關係類型"=\'義近\' AND ' +
# 			'"寅"."腔口"=$3 '
# 			'ORDER BY "寅"."流水號"')(原來腔口, 型態, 欲揣腔口)
# 		print(型態)
		組陣列=[]
		結果=self.查型體翻譯著(原來腔口, 型態, 欲揣腔口)
		for 型體,音標 in 結果:
# 			print(型體,音標)
			組陣列.append(self.分析器.產生對齊組(型體,音標))
			#以後愛提掉
		if 欲揣腔口.startswith(閩南語):
			結果=self.揣台華型體('%;'+型態+';%')
			for 型體,音標 in 結果:
				if 音標.strip()!='':
					新音標=self.粗胚工具.建立物件語句前處理減號(教會羅馬字音標, 音標)
					原來組=self.分析器.產生對齊組(型體,新音標)
					標準組=self.家私.組轉做標準音標(教會羅馬字音標, 原來組)
					組陣列.append(標準組)
		return 組陣列
# 
# 型體翻譯 = lambda 原來腔口, 型態, 欲揣腔口:資料庫連線.prepare('SELECT ' +
# 	'"寅"."流水號","寅"."來源","寅"."種類","寅"."腔口","寅"."地區","寅"."年代",'+
# 	'"寅"."組合","寅"."型體","寅"."音標","寅"."調變","寅"."音變" ' +
# 	'FROM "言語"."文字" AS "子", "言語"."關係" AS "丑", "言語"."文字" AS "寅" ' +
# 	' WHERE "子"."腔口"=$1 AND "子"."型體"=$2 AND ' +
# 	'"丑"."乙流水號"="子"."流水號" AND "丑"."甲流水號"="寅"."流水號" AND "丑"."乙對甲的關係類型"=\'義近\' AND ' +
# 	'"寅"."腔口" LIKE $3 '
# 	'ORDER BY "寅"."流水號"')(原來腔口, 型態, 欲揣腔口)
# 
# 型體似義 = lambda 原來腔口, 型態, 欲揣腔口:資料庫連線.prepare('SELECT ' +
# 	'"寅"."流水號","寅"."來源","寅"."種類","寅"."腔口","寅"."地區","寅"."年代",'+
# 	'"寅"."組合","寅"."型體","寅"."音標","寅"."調變","寅"."音變" ' +
# 	'FROM "言語"."文字" AS "子", "言語"."關係" AS "丑", "言語"."文字" AS "寅" ' +
# 	' WHERE "子"."腔口"=$1 AND "子"."型體" LIKE $2 AND ' +
# 	'"丑"."乙流水號"="子"."流水號" AND "丑"."甲流水號"="寅"."流水號" AND "丑"."乙對甲的關係類型"=\'義近\' AND ' +
# 	'"寅"."腔口"=$3 '
# 	'ORDER BY "寅"."流水號"')(原來腔口, '%'+型態+'%', 欲揣腔口)
# 型體似義 = lambda 原來腔口, 型態, 欲揣腔口:資料庫連線.prepare('SELECT ' +
# 	'"寅"."流水號","寅"."來源","寅"."種類","寅"."腔口","寅"."地區","寅"."年代",'+
# 	'"寅"."組合","寅"."型體","寅"."音標","寅"."調變","寅"."音變" ' +
# 	'FROM "言語"."文字" AS "子", "言語"."關係" AS "丑", "言語"."文字" AS "寅" ' +
# 	' WHERE "子"."腔口"=$1 AND "子"."型體" LIKE $2 AND ' +
# 	'"丑"."乙流水號"="子"."流水號" AND "丑"."甲流水號"="寅"."流水號" AND "丑"."乙對甲的關係類型"=\'義近\' AND ' +
# 	'"寅"."腔口"=$3 '
# 	'ORDER BY "寅"."流水號"')(原來腔口, 型態+'%', 欲揣腔口)
# 
# 揣型體 = lambda 原來腔口, 型態:資料庫連線.prepare('SELECT ' +
# 	'"子"."流水號","子"."來源","子"."種類","子"."腔口","子"."地區","子"."年代",'+
# 	'"子"."組合","子"."型體","子"."音標","子"."調變","子"."音變" ' +
# 	'FROM "言語"."文字" AS "子" ' +
# 	' WHERE "子"."腔口" LIKE $1 AND "子"."型體"=$2 '+
# 	'ORDER BY "子"."流水號"')(原來腔口, 型態)
# 	

# if __name__ == '__main__':
# 	print(型體翻譯('漢語族官話方言北京官話臺灣腔', '一朵花', '漢語族閩方言閩南語偏漳優勢音'))
# 	print(型體翻譯('漢語族官話方言北京官話臺灣腔', '多', '漢語族閩方言閩南語偏漳優勢音'))



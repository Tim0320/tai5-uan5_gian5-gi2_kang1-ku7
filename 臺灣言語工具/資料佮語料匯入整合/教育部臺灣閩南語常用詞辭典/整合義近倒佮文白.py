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
from 臺灣言語工具.資料庫.整合.教育部閩南語常用詞辭典 import 揣義倒詞組合
from 臺灣言語工具.資料庫.整合.教育部閩南語常用詞辭典 import 用來源主號碼揣流水號
from 臺灣言語工具.資料庫.整合.整合入言語 import 加關係
from 臺灣言語工具.資料庫.欄位資訊 import 會當替換
from 臺灣言語工具.資料庫.欄位資訊 import 義倒
from 臺灣言語工具.資料庫.欄位資訊 import 義近
from 臺灣言語工具.資料庫.整合.教育部閩南語常用詞辭典 import 揣義近詞組合
from 臺灣言語工具.資料庫.整合.教育部閩南語常用詞辭典 import 揣文白流水號

class 整合義近倒後佮文白():
	def __init__(self):
		for 甲主編號, 乙主編號 in 揣義倒詞組合():
			甲流水號 = 用來源主號碼揣流水號(甲主編號)
			乙流水號 = 用來源主號碼揣流水號(乙主編號)
			for 甲 in 甲流水號:
				for 乙 in 乙流水號:
		#			print(str(甲) + ' ' + str(乙) + '義倒')
					加關係(甲[0], 乙[0], 義倒, 會當替換)
					加關係(乙[0], 甲[0], 義倒, 會當替換)
		for 甲主編號, 乙主編號 in 揣義近詞組合():
			甲流水號 = 用來源主號碼揣流水號(甲主編號)
			乙流水號 = 用來源主號碼揣流水號(乙主編號)
			for 甲 in 甲流水號:
				for 乙 in 乙流水號:
		#			print(str(甲) + ' ' + str(乙) + '義近')
					加關係(甲[0], 乙[0], 義近, 會當替換)
					加關係(乙[0], 甲[0], 義近, 會當替換)
		文白對應 = lambda 文白: '文讀層' if 文白 == '文' else '白話層'
		頭前的字 = None
		頭前的流水號 = []
		print(揣文白流水號())
		for 主編號, 字, 文白 in 揣文白流水號():
			這馬字流水號 = 用來源主號碼揣流水號(主編號)
		#	print(str(主編號) + ' '+ 字+ ' '+ 文白)
		#	print (這馬字流水號)
			if 頭前的字 == 字:
				for 頭前字, 頭前文白 in 頭前的流水號:
					for 這馬流水號 in 這馬字流水號:
		#				print(str(頭前字) + ' ' + str(這馬流水號) + ' ' + '仝字，用佇無仝言語層' + ' ' + 文白對應(文白))
						加關係(頭前字, 這馬流水號[0], '仝字，用佇無仝言語層', 文白對應(文白))
						加關係(這馬流水號[0], 頭前字, '仝字，用佇無仝言語層', 文白對應(頭前文白))
			else:
				頭前的流水號 = []
			頭前的字 = 字
			for 這馬流水號 in 這馬字流水號:
				頭前的流水號.append((這馬流水號[0], 文白))

if __name__ == '__main__':
	整合義近倒後佮文白()

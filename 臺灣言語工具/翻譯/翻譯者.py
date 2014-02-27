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
from 臺灣言語工具.資料庫.查資料庫 import 查資料庫
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.基本元素.句 import 句
from 臺灣言語工具.字詞組集句章.基本元素.章 import 章
from 臺灣言語工具.字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
import Pyro4

class 翻譯者():
	查資料 = 查資料庫()
	標音工具 = Pyro4.Proxy("PYRONAME:內部自動標音")
	# 台華詞典用
	譀鏡 = 物件譀鏡()
	def 翻譯章物件(self, 原來腔口, 欲揣腔口, 章物件):
		#print( 原來腔口, 欲揣腔口, 章物件)
		句陣列 = []
		for 句物件 in 章物件.內底句:
			集陣列 = []
			for 集物件 in 句物件.內底集:
				組陣列 = []
				for 組物件 in 集物件.內底組:
					for 詞物件 in 組物件.內底詞:
						組陣列.extend(
							self.查資料.型體翻譯著(原來腔口,
							self.譀鏡.看型(詞物件), 欲揣腔口))
				#print(組物件,組陣列)
				if len(組陣列)==0:
					標音章物件=self.標音工具.語句斷詞標音(欲揣腔口, self.譀鏡.看型(詞物件))
					for 標音句物件 in 標音章物件.內底句:
						集陣列.extend(標音句物件.內底集)
				else:
					集陣列.append(集(組陣列))
			句陣列.append(句(集陣列))
		翻譯了章物件 = 章(句陣列)
		return 翻譯了章物件

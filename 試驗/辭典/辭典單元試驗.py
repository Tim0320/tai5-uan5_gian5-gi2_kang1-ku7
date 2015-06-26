# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤


class 辭典單元試驗:
    辭典型態 = None

    def setUp(self):
        self.字典 = self.辭典型態(4)
        self.粗胚 = 文章粗胚()
        self.分析器 = 拆文分析器()
        self.孤詞物 = self.分析器.建立詞物件('你')
        self.孤詞音 = self.分析器.建立詞物件('li2')
        self.二詞物 = self.分析器.建立詞物件('好')
        self.二詞音 = self.分析器.建立詞物件('ho2')
        self.短詞物 = self.分析器.建立詞物件('你好')
        self.短詞音 = self.分析器.建立詞物件('li2-ho2')
        self.詞物件 = self.分析器.建立詞物件('你好無？')
        self.詞音標 = self.分析器.建立詞物件('li2-ho2-bo5-?')
        self.對齊詞 = self.分析器.產生對齊詞('你好無？', 'li2-ho2-bo5-?')
        self.偏泉詞 = self.分析器.產生對齊詞('你好無？', 'lu2-ho2-bo5-?')
        self.無仝詞 = self.分析器.產生對齊詞('你有無？', 'li2-u7-bo5-?')
        self.傷長詞 = self.分析器.產生對齊詞('你有好無？', 'li2-u7-ho2-bo5-?')

    def tearDown(self):
        pass

    def test_漢字加詞成功無(self):
        self.字典.加詞(self.詞物件)
        self.assertEqual(
            self.字典.查詞(self.詞物件), [set(), set(), set(), {self.詞物件}])

    def test_多對齊加詞成功無(self):
        self.字典.加詞(self.對齊詞)
        self.字典.加詞(self.對齊詞)
        self.assertEqual(
            self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])

    def test_查對齊詞成功無(self):
        self.字典.加詞(self.對齊詞)
        self.assertEqual(
            self.字典.查詞(self.詞物件), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.詞音標), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(self.字典.查詞(self.無仝詞), [set(), set(), set(), set()])

    def test_相近詞無使查著(self):
        self.字典.加詞(self.無仝詞)
        self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), set()])
        self.assertEqual(len(self.詞音標.內底字), 4)
        self.assertEqual(self.字典.查詞(self.詞音標), [set(), set(), set(), set()])
        self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), set()])
        self.assertEqual(
            self.字典.查詞(self.無仝詞), [set(), set(), set(), {self.無仝詞}])

    def test_傷長詞無使查著(self):
        self.字典.加詞(self.對齊詞)
        self.字典.加詞(self.傷長詞)
        self.assertEqual(
            self.字典.查詞(self.詞物件), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.詞音標), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.傷長詞), [set(), set(), set(), set(), set()])

    def test_長短詞攏愛揣出來(self):
        self.字典.加詞(self.孤詞物)
        self.字典.加詞(self.二詞物)
        self.字典.加詞(self.短詞物)
        self.字典.加詞(self.詞物件)
        self.字典.加詞(self.孤詞音)
        self.字典.加詞(self.二詞音)
        self.字典.加詞(self.短詞音)
        self.字典.加詞(self.詞音標)
        self.assertEqual(self.字典.查詞(self.詞物件),
                         [{self.孤詞物}, {self.短詞物}, set(), {self.詞物件}])
        self.assertEqual(self.字典.查詞(self.詞音標),
                         [{self.孤詞音}, {self.短詞音}, set(), {self.詞音標}])

    def test_仝款長度有兩个以上(self):
        self.字典.加詞(self.詞物件)
        self.字典.加詞(self.對齊詞)
        self.字典.加詞(self.偏泉詞)
        self.assertEqual(self.字典.查詞(self.詞物件),
                         [set(), set(), set(), {self.詞物件, self.對齊詞, self.偏泉詞}])
        self.assertEqual(self.字典.查詞(self.詞音標),
                         [set(), set(), set(), {self.對齊詞}])

    def test_長度零的詞愛錯誤(self):
        self.assertRaises(解析錯誤, self.字典.加詞, 詞())

    def test_零連詞(self):
        self.assertRaises(參數錯誤, self.辭典型態, 0)
        self.assertRaises(參數錯誤, self.辭典型態, -10)

    def test_字數(self):
        for 長度 in range(1, 100):
            self.assertEqual(self.辭典型態(長度).上濟字數(), 長度)

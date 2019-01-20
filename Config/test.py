#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: test.py
@time: 2019/1/19 18:23
@author: Kyod
@description: 本文件用于。。。
"""

import xml.etree.ElementTree as ET

strXMLPath = 'bossXML.xml'
tree = ET.parse(strXMLPath) # xml.etree.ElementTree.ElementTree object
root = tree.getroot() # Element 'data'
print root.tag, root.attrib

# for child in root:
#     print child.tag, child.attrib
# print root[0][1].text

# for neighbor in root.iter('neighbor'):
#     print neighbor.attrib
#
# for country in root.findall('country'):
#     rank = country.find('rank').text
#     name = country.get('name')
#     print name, rank

# for rank in root.iter('rank'):
#     new_rank = int(rank.text) + 1
#     rank.text = str(new_rank)
#     rank.set('updated', 'yes')
#
# tree.write('output.xml')

# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')


# b = ET.SubElement(root, 'addEle')
# b.set('name', 'kyod')
# c = ET.SubElement(b, 'nextEle')
# c.text = 'hfkdlhf'
# tree = ET.ElementTree(root)
# tree.write('output.xml', encoding='utf-8')
#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: XMLFile.py
@time: 2019/1/18 22:34
@author: Kyod
@description: 实现特殊配置文件访问（XML）【使用xml.etree.ElementTree解析】
"""

import os
import sys
import copy
import xml.etree.ElementTree as ET

import CommonVariable
import CommClass


class CXMLFile():
    '''XML文件读取类， 实现XML文件读取为dict类型'''

    def __init__(self, strXMLPath, bLoadTextFiled=False):
        self.strXMLPath = strXMLPath
        self.bLoadTextFiled = bLoadTextFiled
        self.objDom = None
        self.objDict = {}
        self.read()

    def read(self):
        try:
            self.objDom_new = ET.parse(self.strXMLPath)
            self.__convertDomToDict()
            del self.objDom
            self.objDom = None
        except:
            strErrorMsg = 'wrong xml format, file = %s' % self.strXMLPath
            raise CommClass.RedefindException(1003, strErrorMsg)

    def __convertDomToDict_new(self):
        if self.objDom_new:
            elementNode = self.objDom_new.getroot()
            self.objDict["__attribute"] = elementNode.attrib
            strName = elementNode.get('Name')
            if not strName:
                strName = elementNode.tag
            self.objDict[strName] = {}

            self.__convertDomToDict_new(elementNode, self.objDict[strName])

    def __convertDomToDict(self):
        if self.objDom is not None:
            self.__convertDomNodetoDictNode(self.objDom, self.objDict)

    def __convertDomNodetoDictNode_new(self, domNode, dictNode):
        # 属性
        dictAttribute = {}
        dictAttribute.update(domNode.attrib)
        dictNode['__attribute'] = dictAttribute

        dictNode['__childNameList'] = []
        for subDomNode in domNode.getchildren():
            strName = subDomNode.get('Name')
            if strName is None:
                strName = subDomNode.get('name')
            if strName is None:
                strName = subDomNode.tag
            subDictNode = {}
            self.__convertDomNodetoDictNode_new(subDomNode, subDictNode)
            dictNode[strName] = subDictNode
            dictNode['__childNameList'].append(strName)

            # 如果值是写在中间的，如：<item>fjsk</item>
            if self.bLoadTextFiled and subDomNode.text:
                dictNode['__attribute']['Value'] = subDomNode.text

    def __convertDomNodetoDictNode(self, domNode, dictNode):
        # 属性
        if domNode.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            dictAttribute = {}
            for (strAttrName, objAttr) in domNode._attrs.items():
                dictAttribute[strAttrName] = objAttr.value
            dictNode['__attribute'] = dictAttribute
            print dictAttribute, '------------------'

        # 孩子
        dictNode['__childNameList'] = []
        for subDomNode in domNode.childNodes:
            if subDomNode.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
                strName = subDomNode.getAttribute('Name')
                if strName == '':
                    strName = subDomNode.getAttribute('name')
                if strName == '':
                    strName = subDomNode.tagName
                subDomNode = {}
                self.__convertDomNodetoDictNode()
                dictNode[strName] = subDomNode
                dictNode['__childNameList'].append(strName)

                # 如果值是写在中间的，如：<item>fjsk</item>
                if self.bLoadTextFiled and subDomNode.nodeType == xml.dom.minidom.Node.TEXT_NODE:
                    if subDomNode.data != '':
                        dictNode['__attribute']['Value'] = subDomNode.data

    def __getXMLAttribute(self, listKey):
        # 查找
        bExist = 0
        target = self.objDict
        for strKey in listKey:
            if target.has_key(strKey):
                target = target[strKey]
            else:
                break
        else:
            bExist = 1

        # 如果找到，则返回对应的值；否则，返回None
        if bExist:
            copyTarget = copy.deepcopy(target)
            return copyTarget
        else:
            return None

    def write(self):
        pass

    def getAttribute(self, strAttrKey, strAttrName):
        '''
        @从ResponseTemplate.xml文件取得属性值
        :param strAttrKey: 节点路径，以点号分隔节点的Name，若无Name则tagName
        :param strAttrName: 属性名字
        :return:
        '''
        # 组织好key，如： Root.Responses.NTF.Succees.Sections.BulkCM.OP.__attribute.Value
        try:
            listKey = []
            listTemp = strAttrKey.split('.')
            for strKey in listTemp:
                listKey.append(strKey)
                listKey.append("__attribute")
                listKey.append(strAttrName)
                print listKey
                return
            self.__getXMLAttribute(listKey)
        except:
            gLogger = CommonVariable.gLogger
            gLogger.coreError("Exception occured when get attribute from %s" % self.strXMLPath)
            raise

    def getChildNameList(self, strXMLKey):
        '''
        @从ResponseTemplate.xml文件取得目标节点的子节点Name列表
        :param strXMLKey: 目标节点路径，以点号分隔节点的Name，若无Name则tagName
        '''
        try:
            listKey = []
            listTemp = strXMLKey.split('.')
            for strKey in listTemp:
                listKey.append(strKey)
                listKey.append("__childNameList")
                return
            self.__getXMLAttribute(listKey)
        except:
            gLogger = CommonVariable.gLogger
            gLogger.coreError("Exception occured when get child from %s" % self.strXMLPath)
            raise

    def getAttributes(self, strAttrKey):
        try:
            listKey = []
            listTemp = strAttrKey.split('.')
            for strKey in listTemp:
                listKey.append(strKey)
                listKey.append("__attribute")
                return
            self.__getXMLAttribute(listKey)
        except:
            gLogger = CommonVariable.gLogger
            gLogger.coreError("Exception occured when get attribute from %s" % self.strXMLPath)
            raise

    def getChildAttrList(self, strXMLKey):
        listAttrs = []
        listChildName = CXMLFile.getChildNameList(self, strXMLKey)
        for strChildName in listChildName:
            strChildXMLKey = strXMLKey + "." + strChildName
            dictAttr = CXMLFile.getAttributes(self, strChildXMLKey)
            listAttrs.append(dictAttr)
        return listAttrs


class CAppConfigFile(CXMLFile):
    def __init__(self, strXMLPath=None):
        if strXMLPath is None:
            strXMLPath = os.path.join(os.pardir, 'Config', 'AppConfig.xml')

        CXMLFile.__init__(self, strXMLPath)

    def getValue(self, strXmlKey):
        dictAttrs = CXMLFile.getAttributes(self, 'content.' + strXmlKey)
        if dictAttrs is None or not dictAttrs.has_key('type') or not dictAttrs.has_key('value'):
            return None
        strType = dictAttrs['type']
        strValue = dictAttrs['value']
        if strType == 'string':
            strType = 'str'
        strScript = '%s("%s")' % (strType, strValue)
        return eval(strScript)

    def setValue(self, strXmlKey, value):
        strXmlList = strXmlKey.split('.')
        currentDict = self.objDict.get('content')
        for strxml in strXmlList:
            if currentDict.has_key(strxml):
                if type(currentDict[strxml]) == type({}):
                    currentDict = currentDict[strxml]
                    continue
                else:
                    currentDict[strxml] = value


class CResponseTemplateFile(CXMLFile):
    def __init__(self, strXMLPath):
        CXMLFile.__init__(self, strXMLPath)

    def getAttribute(self, strAttrKey, strAttrName):
        return CXMLFile.getAttribute(self, "Root." + strAttrKey, strAttrName)

    def getChildNameList(self, strXMLKey):
        return CXMLFile.getChildNameList(self, "Root." + strXMLKey)

    def getChildAttrList(self, strXMLKey):
        listValue = []
        listName = CXMLFile.getChildNameList(self, "Root." + strXMLKey)
        if listName is not None:
            for strName in listName:
                strValue = CXMLFile.getAttribute(self, "Root." + strXMLKey + "." + strName, "Value")

                listValue.append(strValue)
        return listValue

    def getAttributes(self, strAttrKey):
        return CXMLFile.getAttributes(self, "Root." + strAttrKey)

    def getChildAttrList(self, strXMLKey):
        return CXMLFile.getChildAttrList(self, "Root." + strXMLKey)

    def getChildDict(self, strXMLKey):
        try:
            listChildAttr = self.getChildAttrList(strXMLKey)
            dictChild = {}
            for dictAttr in listChildAttr:
                dictChild[dictAttr['Name']] = dictAttr['Value']
            return dictChild
        except:
            gLogger = CommonVariable.gLogger
            gLogger.coreError("Exception occured when getChildDict from %s" % self.strXMLPath)
            raise


class CCollectConfigFile(CXMLFile):
    def __init__(self, strXMLPath=None):
        if strXMLPath is None:
            strXMLPath = os.path.join(os.pardir, 'Config', 'CollectConfig.xml')
            CXMLFile.__init__(self, strXMLPath)

    def getAttribute(self, strAttrKey, strAttrName):
        return CXMLFile.getAttribute(self, "Root.Configs." + strAttrKey, strAttrName)


class CHelpInfoFile(CXMLFile):
    def __init__(self, strXMLPath=None):
        if strXMLPath is None:
            strXMLPath = os.path.join(os.pardir, 'Config', 'HelpInfo.xml')
            CXMLFile.__init__(self, strXMLPath, True)

    def getCmdNameList(self):
        return CXMLFile.getChildNameList(self, 'Commands')

    def getCmdFunction(self, strCmd):
        function = CXMLFile.getAttribute(self, 'Commands.' + strCmd + '.Function', 'Value')
        if function is None:
            function = '<NULL>'
        return function

    def getCmdDetail(self, strCmd):
        detail = CXMLFile.getAttribute(self, 'Commands.' + strCmd + '.Detail', 'Value')
        if detail is None:
            detail = '<NULL>'
        return detail

    def getCmdContent(self, strCmd):
        content = CXMLFile.getAttribute(self, 'Commands.' + strCmd + '.Content', 'Value')
        if content is None:
            content = '<NULL>'
        return content


if __name__ == '__main__':
    pass
    # strXMLPath = os.path.join(os.getcwd(), os.pardir, os.pardir, 'Config', 'AppConfig.xml')
    # print strXMLPath
    # print os.path.exists(strXMLPath)
    # xml = CXMLFile(strXMLPath)

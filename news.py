import xml.etree.ElementTree as ET
import operator
from collections import Counter
import json

def parsing_json(filenames):
    with open(filenames, encoding='utf-8') as datafile:
        json_data = json.load(datafile)
        composition = list()
        for i in range(len(json_data['rss']['channel']['items'])):

            str = json_data['rss']['channel']['items'][i]['description']
            for rez in str.split(' '):
                if len(rez) > 6:
                    composition.append(rez.lower())
    return composition

def parsing_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    xml_items = root.findall("channel/item/description")
    composition=list()
    set_words=set()
    for xmli in xml_items:

        for i in xmli.text.split(' '):
            if len(i) > 6:
                composition.append(i.lower())
    return composition

def switch_top_news ( filenames, type):
    if type == 'XML':
        compositions = parsing_xml(filenames)
        #print('XML')
    if type == 'JSON':
        compositions = parsing_json(filenames)


    set_words = set(compositions)
    dict_words={}
    for i in set_words:
        #print(i,compositions.count(i))
        dict_words[i] = compositions.count(i)
    #print (dict_words)
    dict_com={}
    for key,val in sorted(dict_words.items(), key=operator.itemgetter(1),reverse=True ):

        dict_com[key]=val
    #print (dict_com)
    print('===============================================')
    print('===========Код самостоятельный ================')
    print('=====  file = {}====================='.format (filenames))
    print('===============================================')
    k=0
    for key,val in dict_com.items():
        k+=1
        if k<=10:
            print(key,val)
        else:
            break

def switch_news_counter(filenames, type):
    if type == 'XML':
        compositions = parsing_xml(filenames)
        #print('XML')
    if type == 'JSON':
        compositions = parsing_json(filenames)

    Counter(compositions)
    dict_count=Counter(compositions)
    print('===============================================')
    print('===========Код c помощью библиотеки ===========')
    print('=====  file = {}====================='.format(filenames))
    print('===============================================')
    print(dict_count.most_common(10))


def run_top_news(filenames,type):
    switch_top_news(filenames,type)


if __name__== '__main__':

    run_top_news('newsafr1.xml','XML')

    switch_news_counter('newsafr1.xml','XML')

    run_top_news('newsafr.json','JSON')

    switch_news_counter('newsafr.json','JSON')











# f = open('test.txt')
# temp = f.read().splitlines()
# list = [x.strip(' ') for x in temp]
# temp = list(map(str.strip,temp))
# print(temp)
import json

# json_data = json.loads(open('testcases.json').read())
# #print(json_data)
# tree = []
# tree1 = dict('module'['class'['testcase'[]]])
# for module in json_data:
#     tree1['module'].append(module)
#     #print('\n Module Name:', module)
#     for classs in json_data[module]:
#         tree1[module].append(classs)
#      #   print('\n \t', 'Class Name:', classs)
#         for testcase_list in json_data[module][classs]:
#             #tree1['test_case'].append(testcase_list)
#
#             for testcase in json_data[module][classs][testcase_list]:
#                 #print('\t' * 2, testcase, end=' ')
#                 tree1[module][class].append(testcase)
# print(tree1)
import os

from flask import Flask, render_template
from past.builtins import xrange

" Read JSON file and change its to an intermediate format which Jquery use for displaying tree view on web"
moduleid = 0
json_data = json.loads(open('testcases.json').read())
file = open("hello.json", 'w')
file.write("[")
for module in json_data:
    if moduleid == 0:
        line = "{"+'"id": "{0}", "parent": "#", "text":"{1}"'.format(moduleid, module)+"},\n"
    else:
        line = ",{" + '"id": "{0}", "parent": "#", "text":"{1}"'.format(moduleid, module) + "},\n"
    file.write(line)
    classid = 0
    for classs in json_data[module]:
        id = (moduleid, classid)  # purpose of this tuple is that id will be unique.
        if classid ==0:
            line2 = "{" + '"id": "{0}", "parent":"{1}", "text": "{2}", "parentname": "{3}"'.format(id, moduleid, classs,module) + "}"
        else:
            line2 = ",{" + '"id": "{0}", "parent":"{1}", "text": "{2}"'.format(id, moduleid, classs) + "}"
        classid += 1
        file.write(line2)
        testcaseid = 0
        for testcase_list in json_data[module][classs]:
            for testcase_name in json_data[module][classs][testcase_list]:
                testid = (moduleid, classid, testcaseid)
                line3 = ",\n{"+'"id": "{0}", "parent": "{1}", "text": "{2}","parentname": "{3}"'.format(testid, id, testcase_name,classs)+"}"
                file.write(line3)
                testcaseid += 1
    moduleid += 1
file.write("]")
file.close()



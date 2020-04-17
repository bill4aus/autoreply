#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append("..")
import functions
import setting

# categories=bidict({
#     '财经': 0,
#     '时政': 1,
# })


#删除已经分词的文档
fdlist = functions.getFolderPathList('../segment')
for fdname in fdlist:
    flist = functions.getFilePathList(fdname)
    print(flist)
    for fname in flist:
        os.remove(fname)


# #删除未分词的文档
# fdlist = functions.getFolderPathList('../corpus')
# for fdname in fdlist:
#     flist = functions.getFilePathList(fdname)
#     print(flist)
#     for fname in flist:
#         os.remove(fname)


# #删除所有目录
# fdlist = functions.getFolderPathList('../segment')
# for fdname in fdlist:
#     # os.chmod(fdname,7777)
#     os.remove(fdname)
# fdlist = functions.getFolderPathList('../corpus')
# for fdname in fdlist:
#     os.remove(fdname)  


# #重新建立所有目录
# os.makedirs(path)

# for catename in setting.categories:
#     os.makedirs('../segment/'+catename)
#     os.makedirs('../corpus/'+catename)
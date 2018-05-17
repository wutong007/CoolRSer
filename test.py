# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

session_item_data=[[100, [10, 11], [12, 13]],
                   [101, [11, 12], [10, 14]],
                   [102, [10, 13, 14], [11, 15]]]

# for curr in session_item_data:
#     print(curr[0])
#
# session_index_dic=dict()
# for i in range(len(session_item_data)):
#     d = session_item_data[i][0]
#     # print(d)
#     session_index_dic[d] = i
#
# print(session_index_dic)



session_item_data_dict=dict()
for i in range(len(session_item_data)):
    d = session_item_data[i][0]
    print("session_id为：",d)
    session_item_data_dict[d]=[[],[]]
    session_item_data_dict[d][0]=session_item_data[i][1]
    session_item_data_dict[d][1]=session_item_data[i][2]
print(session_item_data_dict)


# 0515:juansiwei
# -*- coding: utf-8 -*-
import Common
import time
graph = {'cangan': set(['tianche', 'fomen','guojing']),
         'guojing': set(['jingwai', 'putuo', 'cangan']),
         'jingwai': set(['pansi', 'wushi','nver','difu']),
         'wushi': set(['wuzhuang','mowang','linxian','wansou','jingwai' ]),
         'linxian': set(['wushi','kunlun','fangcun']),
         'kunlun': set(['tiangong','beiming','huaguo']),
         'huaguo': set(['aolai','kunlun']),
         'aolai': set(['zhenwai', 'tianmo','huaguo']),
         'tianmo': set(['yunyin']),
         'zhenwai': set(['aolai', 'longgong','qinghe']),
         'chengwai': set(['cangan', 'qinghe']),
         'qinghe': set(['chengwai','zhenwai']),
         'wansou': set(['shiwang']),
         'wuzhuang': set(['qiankun'])}
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                print(next)
                time.sleep(1)
                queue.append((next, path + [next]))
a=list(bfs_paths(graph, 'cangan', 'qiankun')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
print(a)
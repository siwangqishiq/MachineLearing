from numpy import *
import operator

#创建操作数据集
def createDataSet():
    group = array([
                    [1.0,1.1],
                    [1.0,1.0],
                    [0.0,0.0],
                    [0.0,0.1]
                ])
    labels = ['A','A','B','B']
    print("create Data Set!")
    return group , labels

def classify0(inX , dataSet , labels , k):
    dataSetSize = dataSet.shape[0] #查看矩阵或者数组的维数
    diffMat = tile(inX , (dataSetSize , 1)) - dataSet
    #print(diffMat)
    sqDiffMat = diffMat ** 2;
    #print(sqDiffMat)
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance ** 0.5
    print("distance = %s" %distances)
    sort_distances_index = distances.argsort()
    print("排序后的数组索引 sort_distances = %s" %sort_distances_index)

    class_count = {}
    for i in range(k):
        #print("i = %d" %i)
        vote_labels_index = labels[sort_distances_index[i]]
        class_count[vote_labels_index] = class_count.get(vote_labels_index , 0) + 1
    print("class_count = %s" %(class_count))
    #按字典的value值排序
    sort_class_count = sorted(class_count.items(),
                              key = operator.itemgetter(1),reverse=True)
    print("sort_class_count = %s" %(sort_class_count))
    return sort_class_count[0][0]

def main():
    #testMat()
    dataSet = createDataSet();
    last_tag = classify0([0,0] , dataSet[0] , dataSet[1] , 3)
    print("result = %s" %(last_tag))

main();
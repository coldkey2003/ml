'''

>>> from sklearn import tree
>>> X = [[0, 0], [1, 1]]
>>> Y = [0, 1]
>>> clf = tree.DecisionTreeClassifier()
>>> clf = clf.fit(X, Y)__author__ = 'zhaojia'
>>> clf.predict([[2., 2.]])
array([1])
>>> clf.predict_proba([[2., 2.]])
array([[ 0.,  1.]])
>>> from sklearn.datasets import load_iris
>>> from sklearn import tree
>>> iris = load_iris()
>>> clf = tree.DecisionTreeClassifier()
>>> clf = clf.fit(iris.data, iris.target)

'''

class Options(object):
    def __init__(self):
        self.criterion = 'gini'
        self.max_depth = '8'
        self.min_samples_leaf = 2
        self.max_leaf_nodes = 100

class tree(object):
    def __init__(self, config):
        self.criterion = config.criterion
        self.max_depth = config.max_depth
        self.min_samples_leaf = config.min_samples_leaf
        self.max_leaf_nodes = config.max_leaf_nodes

    #TODO
    def gini_index(self, attr, label):
        return 0

    def get_attr_importance_value(self, metric_type, attr, label):
        if metric_type == 'gini':
            return self.gini_index(attr, label)

    #TODO
    def choose_best_attr(self, attr_list, label):
        pass

    #TODO
    def build_tree(self):
        pass

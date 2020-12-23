## Simple KNN
This is a KNN implementation in python.

### Usage

```py
train_x = [(0, 0), (0, 1), (1, 1), (15, 16), (15, 17)]
train_y = ['class1', 'class1', 'class1', 'class2', 'class2']

test_x = [(2, 0), (1, 0), (16, 16)]
knn = KNN(K=3)

knn.fit(train_x, train_y)
knn.predict(test_x)
```

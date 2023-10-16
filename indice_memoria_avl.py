import csv_cols

class Node:
    def __init__(self, key, position):
        self.key = key
        self.positions = [position]
        self.height = 1
        self.left = None
        self.right = None

class AVLIndice:
    def __init__(self, fileName):
        self.root = None

        self.fileName = fileName

        with open(fileName, 'rb') as f:
            while True:
                index = f.tell()
                registro = f.readline()
                
                if not registro:
                    break
                
                registro = registro.decode('utf-8').rstrip('\n').split('\,')

                devId = registro[csv_cols.DEVELOPER_ID].strip(' ')
                self.insert(devId, index)

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balanceFactor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _updateHeight(self, node):
        if node is not None:
            node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _rotateRight(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        self._updateHeight(y)
        self._updateHeight(x)

        return x

    def _rotateLeft(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        self._updateHeight(x)
        self._updateHeight(y)

        return y

    def _insert(self, node, key, position):
        if node is None:
            return Node(key, position)

        if key == node.key:
            node.positions.append(position)
            return node

        if key < node.key:
            node.left = self._insert(node.left, key, position)
        else:
            node.right = self._insert(node.right, key, position)

        self._updateHeight(node)

        balance = self._balanceFactor(node)

        if balance > 1:
            if key < node.left.key:
                return self._rotateRight(node)
            else:
                node.left = self._rotateLeft(node.left)
                return self._rotateRight(node)

        if balance < -1:
            if key > node.right.key:
                return self._rotateLeft(node)
            else:
                node.right = self._rotateRight(node.right)
                return self._rotateLeft(node)

        return node

    def insert(self, key, position):
        self.root = self._insert(self.root, key, position)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.positions
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def search(self, key):
        indexRegistros = self._search(self.root, key)

        registers = []

        if indexRegistros is None:
            return registers
        
        with open(self.fileName, 'rb') as f:
            for index in indexRegistros:
                f.seek(index)
                registers.append(f.readline().decode('utf-8').rstrip('\n').split('\,'))
        
        return registers        
            

index = AVLIndice('output.bin')

for app in index.search('BNP Paribas'):
    print(app[csv_cols.APP_NAME], app[csv_cols.DEVELOPER_ID])

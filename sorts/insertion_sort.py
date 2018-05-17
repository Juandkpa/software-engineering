class InsertionSort:

    def __init__(self, _a):
        self.a = _a

    def sort(self):
        '''
        sort main method
        '''
        for j in range(1, len(self.a)):
            key =  self.a[j]
            i = j - 1
            while i >= 0 and self.a[i] > key :
                self.a[i+1] = self.a[i]
                i = i - 1
            self.a[i+1] = key

    def show_sort(self):
        print(self.a)  




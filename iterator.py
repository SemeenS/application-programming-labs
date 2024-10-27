import  csv

class Iterator:

    def __init__(self, csv_path):

        self.csv_path = csv_path
        self.list = self.__load_csv()
        self.limit = len(self.list)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            next_elm = self.csv_path[self.count]
            self.count +=1
            return 1
        else:
            raise StopIteration

    def __load_csv(self) -> list:
        with open(self.csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # skip the header
            path_list = list(row[1] for row in reader)
            return path_list
class SuperList(list):
    def __len__(self):
        return 1000


my_list = SuperList()
print(len(my_list))
my_list.append(5)
print(my_list)
print(issubclass(SuperList, list))

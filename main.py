#12-m
class Computer:
    def __init__(self, model, storage):
        self.model = model
        self.__storage = storage

    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        self.__storage = new_storage

c1 = Computer("Dell", 512)

print(c1.model)
print(c1.get_storage())

c1.set_storage(1024)
print(c1.get_storage())

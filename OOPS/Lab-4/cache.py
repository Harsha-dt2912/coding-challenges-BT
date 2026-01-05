class Cache:
    _MAX_CAPACITY = 0

    @staticmethod
    def get_max_capacity():
        if Cache._MAX_CAPACITY == 0:
            Cache._MAX_CAPACITY = int(input("Enter MAX_CAPACITY: "))
        print("Returning MAX_CAPACITY")
        return Cache._MAX_CAPACITY
        
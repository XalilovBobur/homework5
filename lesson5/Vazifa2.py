class Counter:
    def __init__(self):
        self.count_file = 'count.txt'
        self.update_count()

    def update_count(self):
        try:
            with open(self.count_file, 'r') as file:
                count = int(file.read().strip())
        except FileNotFoundError:
            count = 0

        self.count = count

    def save_count(self):
        with open(self.count_file, 'w') as file:
            file.write(str(self.count))

    def increment_count(self):
        self.count += 1
        self.save_count()

    def get_count(self):
        return self.count



counter = Counter()
print(f"Hozirgi count qiymati: {counter.get_count()}")


counter.increment_count()


print(f"Keyingi count qiymati: {counter.get_count()}")

from abc import ABC, abstractmethod

class maxNumberBase(ABC):
    @abstractmethod
    def add(self, n):
        pass

    @abstractmethod
    def get_max(self):
        pass

    @abstractmethod
    def remove_max(self):
        pass

class maxNumber(maxNumberBase):
    def __init__(self, numbers=None):
        self.numbers = list(numbers) if numbers is not None else []

    def add(self, n):
        self.numbers.append(n)

    def get_max(self):
        if not self.numbers:
            return None
        return max(self.numbers)

    def remove_max(self):
        max_number = self.get_max()
        if max_number is not None:
            self.numbers.remove(max_number)
        return max_number


def main():
    num = int(input("Please enter a digit: "))
    numbers = maxNumber()
    for _ in range(num):
        n = int(input("Enter a number: "))
        numbers.add(n)
    numbers.remove_max()
    print(numbers.numbers)


if __name__ == "__main__":
    main()
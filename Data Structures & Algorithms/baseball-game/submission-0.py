class Solution:
    def is_integer(self, val: str) -> bool:
        try:
            num = int(val)
            return True
        except ValueError:
            return False

    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if self.is_integer(operations[i]):
                record.append(int(operations[i]))
            if operations[i] == '+':
                record.append(record[-1] + record [-2])
            if operations[i] == 'D':
                record.append(record[-1] * 2)
            if operations[i] == 'C':
                record.pop()
        return sum(record)

        
class FibonacciSeries:
    def sum(self, n):
        sum = 0
        if n > 1:
            aux = [0] * (n)
            aux[0] = 0
            aux[1] = 1
            i = 0
            while i < n:
                if i > 1:
                    aux[i] = aux[i - 2] + aux[i - 1]

                sum += aux[i] * aux[i]
                i += 1

        print(sum)


test = FibonacciSeries()
test.sum(11)

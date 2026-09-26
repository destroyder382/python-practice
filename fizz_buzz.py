# LeetCode 412. FizzBuzz
# Дано число n, вернуть список строк 1..n, где кратные 3 -> "Fizz",
# кратные 5 -> "Buzz", кратные и 3 и 5 -> "FizzBuzz", остальные - само число.

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

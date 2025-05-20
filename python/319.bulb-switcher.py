#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** (1 / 2))

        # def count_factors(n):
        #     if n == 1:
        #         return 1

        #     # Count prime factors
        #     factor_counts = {}
        #     i = 2
        #     while i * i <= n:
        #         while n % i == 0:
        #             factor_counts[i] = factor_counts.get(i, 0) + 1
        #             n //= i
        #         i += 1
        #     if n > 1:
        #         factor_counts[n] = 1

        #     # Total factors = product of (count + 1) for each prime factor
        #     result = 1
        #     for count in factor_counts.values():
        #         result *= (count + 1)
        #     return result

        # # The no-bulb and
        # # one bulb case
        # if n <= 1:
        #     return n

        # # The first bulb will always
        # # be left on, so start at 1
        # bulbs: int = 1

        # for i in range(2, n+1):
        #     f_count = count_factors(i)

        #     # Even Factor counts
        #     # will eval to an off state
        #     if f_count % 2 != 0:
        #         bulbs += 1

        # return bulbs


# @lc code=end


# 速度超过 93.52%, 内存超过14.81%
class Person(object):

    def __init__(self, cost):
        self.a_price, self.b_price = cost
        self.a_extra_cost = self.a_price - self.b_price
        self.priority = abs(self.a_extra_cost)
        self.cost = 0


class Solution:

    def twoCitySchedCost(self, costs):
        persons = [
                Person(cost)
                for cost in costs
            ]
        persons.sort(key=lambda x: -x.priority)

        a_n = 0
        b_n = 0
        half = len(costs) // 2
        index = 0
        total_cost = 0
        # 安排
        for person in persons:
            index += 1
            if person.a_extra_cost > 0:
                b_n += 1
                total_cost += person.b_price
            else:
                a_n += 1
                total_cost += person.a_price
            if a_n == half:
                total_cost += sum((
                    person.b_price for person in persons[index:]))
                return total_cost
            if b_n == half:
                total_cost += sum((
                    person.a_price for person in persons[index:]))
                return total_cost


# 速度超过34.26%, 内存超过6.48%
class Solution:

    def twoCitySchedCost(self, costs):
        persons = [
                (cost[0], cost[1], cost[0]-cost[1], abs(cost[0]-cost[1]))
                for cost in costs
            ]
        persons.sort(key=lambda x: -x[3])

        a_n = 0
        b_n = 0
        half = len(costs) // 2
        index = 0
        total_cost = 0
        # 安排
        for person in persons:
            index += 1
            if person[2] > 0:
                b_n += 1
                total_cost += person[1]
            else:
                a_n += 1
                total_cost += person[0]
            if a_n == half:
                total_cost += sum((
                    person[1] for person in persons[index:]))
                return total_cost
            if b_n == half:
                total_cost += sum((
                    person[0] for person in persons[index:]))
                return total_cost


solution = Solution()
assert solution.twoCitySchedCost(
    [[10, 20], [30, 200], [400, 50], [30, 20]]) == 110

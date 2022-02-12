# 这里有 n 门不同的在线课程，他们按从 1 到 n编号。
# 每一门课程有一定的持续上课时间（课程时间）t 以及关闭时间第 d天。
# 一门课要持续学习 t 天直到第 d 天时要完成，你将会从第 1 天开始。
# 给出 n 个在线课程用 (t, d) 对表示。你的任务是找出最多可以修几门课。
# 输入: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# 输出: 3
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        do = []
        time = 0

        def insert(l: List[int], num: int):
            L, R = 0, len(l) - 1
            while L <= R:
                mid = (L + R)//2
                if num >= l[mid]:
                    L = mid + 1
                else:
                    R = mid - 1
            l.insert(R+1, num)

        for lens, ddl in courses:
            if time + lens <= ddl:
                insert(do, lens)
                time += lens
            elif do and lens < do[-1]:
                time += lens - do.pop()
                insert(do, lens)

        return len(do)
# 内置模块队满后将前端自动出队


from collections import deque


q = deque()
q.append(1)     # 队尾进队
q.popleft()     # 队首出队

q.appendleft()  # 队首进队
q.pop()         # 队尾出队


import heapq
from collections import deque

def solve_10845():
    """[Silver IV] 10845번: 큐"""
    print("--- 10845번: 큐 실행 ---")
    N = int(input())
    queue = deque()

    for _ in range(N):
        command = input().split()
        cmd = command[0]
        
        if cmd == "push":
            queue.append(command[1])
        elif cmd == "pop":
            print(queue.popleft() if queue else -1)
        elif cmd == "size":
            print(len(queue))
        elif cmd == "empty":
            print(0 if not queue else 1)
        elif cmd == "front":
            print(queue[0] if queue else -1)
        elif cmd == "back":
            print(queue[-1] if queue else -1)

def solve_11279():
    """[Silver II] 11279번: 최대 힙"""
    print("--- 11279번: 최대 힙 실행 ---")
    N = int(input())
    heap = []

    for _ in range(N):
        x = int(input())
        
        if x == 0:
            if not heap:
                print(0)
            else:
                # 출력 시 다시 양수로 변환
                print(-heapq.heappop(heap))
        else:
            # 최대 힙을 위해 음수로 변환하여 삽입
            heapq.heappush(heap, -x)

def solve_10866():
    """[Silver IV] 10866번: 덱"""
    print("--- 10866번: 덱 실행 ---")
    N = int(input())
    dq = deque()

    for _ in range(N):
        command = input().split()
        cmd = command[0]
        
        if cmd == "push_front":
            dq.appendleft(command[1])
        elif cmd == "push_back":
            dq.append(command[1])
        elif cmd == "pop_front":
            print(dq.popleft() if dq else -1)
        elif cmd == "pop_back":
            print(dq.pop() if dq else -1)
        elif cmd == "size":
            print(len(dq))
        elif cmd == "empty":
            print(0 if not dq else 1)
        elif cmd == "front":
            print(dq[0] if dq else -1)
        elif cmd == "back":
            print(dq[-1] if dq else -1)

if __name__ == "__main__":
    # solve_10845()
    # solve_11279()
    # solve_10866()
    pass
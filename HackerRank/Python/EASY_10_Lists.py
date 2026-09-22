if __name__ == '__main__':
    N = int(input())
    
    arr = []
    
    for i in range(N):
        command = input().split()
        operation = command[0]
        if "insert" == operation:
            arr.insert(int(command[1]), int(command[2]))
        elif "print" == operation:
            print(arr)
        elif "remove" == operation:
            arr.remove(int(command[1]))
        elif "append" == operation:
            arr.append(int(command[1]))
        elif "sort" == operation:
            arr.sort()
        elif "pop" == operation:
            arr.pop()
        elif "reverse" == operation:
            arr.reverse()

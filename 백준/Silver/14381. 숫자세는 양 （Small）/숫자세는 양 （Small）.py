N = int(input())
for i in range(N):
    res = 0
    num = input()
    ans = ""
    # 0인 경우
    if num == "0":
        ans = "INSOMNIA"
    else:
        visited = [False] * 10

        while True:
            if False not in visited:
                break
            res += 1
            ans = res * int(num)

            for k in list(str(ans)):
                k = int(k)
                if not visited[k]:
                    visited[k] = True

    print("Case #" + str(i + 1) + ": " + str(ans))
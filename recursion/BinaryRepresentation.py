def represent_binary(N):
    if N > 1:
        return str(represent_binary(N // 2)) + str(N % 2)
    else:
        return str(N)

print(represent_binary(13))

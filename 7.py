for s in range(9, 0, -1):
    for e in range(9, -1, -1):
        for n in range(9, -1, -1):
            for d in range(9, -1, -1):
                for m in range(9, 0, -1):
                    for o in range(9, -1, -1):
                        for r in range(9, -1, -1):
                            for y in range(9, -1, -1):
                                st = {s, e, n, d, m, o, r, y}
                                if len(st) == 8:
                                    send = 1000 * s + 100 * e + 10 * n + d
                                    more = 1000 * m + 100 * o + 10 * r + e
                                    money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
                                    if send + more == money:
                                        print(send, more, money)

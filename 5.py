for i in range(100000, 999999):
    if str(i)[1] == str(i)[5] and str(i)[2] == str(i)[4]:
        if str(i+1)[1] == str(i+1)[5] and str(i+1)[2] == str(i+1)[4]:
            if str(i + 2)[1] == str(i + 2)[4] and str(i + 2)[2] == str(i + 2)[3]:
                if str(i + 3)[0] == str(i + 3)[5] and str(i + 3)[1] == str(i + 3)[4] and str(i + 3)[2] == str(i + 3)[3]:
                    break
print(i)

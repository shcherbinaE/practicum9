for i in range(10, 99):
    if str(i*i)[1] == str(i)[0] and str(i*i)[2] == str(i)[1] and str(i*i)[0] != str(i)[0] and str(i*i)[0] != str(i)[1]:
        break
print(i*i)
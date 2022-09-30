while True:
    s, t, f = [int(x) for x in input().split()]
    if 0 <= s <= 23 and 1 <= t <= 12 and -5 <= f <= 5:
        break
hr = s + t + f
if hr > 23:
    hr = hr - 24
elif hr < 0:
    hr = 24 - abs(hr)
print(hr)

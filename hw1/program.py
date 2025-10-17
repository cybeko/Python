start = int(input("From: "))
end = int(input("To: "))

if start == end:
    print("Start number cannot equal to end number")
    exit()

while True:
    step = int(input("Step: "))

    if step <= 0:
        print("Step must be greater than 0. Try again")
        continue

    distance = abs(end - start)
    if distance % step != 0:
        print("Step does not divide evenly. Try again")
    else:
        break

if start < end:
    step = abs(step)
else:
    step = -abs(step)

for i in range(start, end + step, step):
    if (step > 0 and i <= end) or (step < 0 and i >= end):
        print(i, end=" ")

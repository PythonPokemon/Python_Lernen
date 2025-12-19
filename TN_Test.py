import time

count=0
while True:
    try:
        count += 1
        time.sleep(0.0000001)
        print(count)
    except KeyboardInterrupt:
        print(f"Deine Zahl ist {count}.")
        break
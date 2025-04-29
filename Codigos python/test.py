import time
print("Begin")

try:
    while True:
        print("A")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Caught exception")
print("End")

        
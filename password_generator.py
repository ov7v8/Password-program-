import random
import time

L1 = ["Ali", "Mustafa"]
L2 = ["1990"]
L3 = ["Messi"]
L4 = ["Nissan"]
L5 = ["Siri"]
L6 = ["Ahmed"]

all_items = L1 + L2 + L3 + L4 + L5 + L6
signs = ["@", "#", "_", "!", "$", "%", "&", "*", "?", "=", "+"]

def make_pwd():
    a = random.choice(all_items)
    b = random.choice(all_items)
    s = random.choice(signs)
    v = f"{random.randint(0,9999):04d}"

    mode = random.randint(1, 5)

    if mode == 1:
        return a + b
    elif mode == 2:
        return a + s + b
    elif mode == 3:
        return a + "_" + b
    elif mode == 4:
        return a + v + "!"
    else:
        return a.lower() + b.upper() + s

start_t = time.time()
results = set()

while len(results) < 50000:
    results.add(make_pwd())

with open("passwords.txt", "w") as out:
    for item in results:
        out.write(item + "\n")

end_t = time.time()

print("Generated", len(results), "passwords")
print("Time elapsed:", round(end_t - start_t, 2), "seconds")

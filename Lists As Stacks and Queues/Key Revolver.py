



from collections import deque
bullet_price = int(input())
barrel = int(input())
current_barrel = barrel

bullet_counter = 0

bullets = [int(bull) for bull in input().split()]
locks = [int(lock) for lock in input().split()]
locks = deque(locks)
intelligence = int(input())


while locks:
    for bullet in reversed(bullets):
        lock = locks[0]
        bullet_counter += 1
        current_barrel -= 1
        if bullet <= lock:
            print("Bang!")
            locks.popleft()
            bullets.pop()
            if current_barrel < 1 and bullets:
                print("Reloading!")
                current_barrel = barrel
            break
        else:
            print("Ping!")
            bullets.pop()
            if current_barrel < 1 and bullets:
                print("Reloading!")
                current_barrel = barrel
    if not locks:
        break
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        exit(0)


if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - bullet_counter * bullet_price}")





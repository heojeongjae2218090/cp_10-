import random
def 생성_로또_번호():
    lotto_numbers =[random.randint(1,45) for _ in range(6)]
    lotto_numbers = list(set(lotto_numbers))
    while len(lotto_numbers) < 6:
        new_number = random.randint(1, 45)
        if new_number not in lotto_numbers:
            lotto_numbers.append(new_number)

    lotto_numbers.sort()
    return lotto_numbers
if __name__ == "__main__":
    생성_번호 = 생성_로또_번호()
print("생성된 로또 번호:", 생성_번호)

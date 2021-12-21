import numpy as np

if __name__ == "__main__":
    def part_updating(number, start_point, pas):
        for i in range(number):
            if pas == 1:
                color = round(i*255/number)
            else:
                color = round(255*(1-i/number))
            palette[start_point+i] = [color, color, color]

    palette = np.zeros((1024, 3), dtype=np.uint8)

    pas = 1
    start_point = 0
    for j in range(1, 11):
        number = 1024//(2**j)
        part_updating(number, start_point, pas)
        start_point += number
        pas *= -1
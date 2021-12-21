from image_creating import toimage, np
from modules import square_loop, convert_speed, jit, convert_speed_2
from time import mktime, gmtime

"""@jit(nopython=True)
def main(data, size_a, size_b, iterations):
    for j in range(0, size_b):
        x, y = 2*(i-size_a/2)/size_a, 2*(j-size_b/2)/size_b
        speed = square_loop(iterations, x, y)
        color = convert_speed(speed, iterations)
        data[i, j] = [color, color, color]"""

if __name__ == "__main__":
    def part_updating(number, start_point, pas):
        for i in range(number):
            if pas == 1:
                color = round(i*255/number)
            else:
                color = round(255*(1-i/number))
            palette[start_point+i] = [0, 0, color]

    palette = np.zeros((4096, 3), dtype=np.uint8)

    pas = 1
    start_point = 0
    for j in range(1, 13):
        number = 4096//(2**j)
        part_updating(number, start_point, pas)
        start_point += number
        pas *= -1

    for photo in range(21):
        start = mktime(gmtime())
        print(f"\n\nstarted computing image number {photo}")
        iterations = 4096
        ratio = 2**photo
        x_centre = -100.012
        y_centre = 500.002
        # Create a 1024x1024x3 array of 8 bit unsigned integers
        size_a = 1080
        size_b = 1920
        data = np.zeros((size_a, size_b, 3), dtype=np.uint8)

        #data[:,960] = [254,255,255]       # Makes the middle pixel red
        #data[540,:] = [254,255,255]       # Makes the next pixel blue
        """x_decline = x_centre/size_b - 1/ratio
        y_decline = - y_centre/size_a - 1/ratio"""
        for i in range(0, size_a):
            for j in range(0, size_b):
                y, x = 2*(i-size_a/2 - y_centre*ratio)/(size_a*ratio), 2*(j-size_b/2 + x_centre*ratio)/(size_b*ratio)    #here could be zoom
                pas, speed = square_loop(iterations, x, y)
                if pas:
                    color = convert_speed_2(speed)
                else:
                    color = convert_speed(speed, iterations)
                data[i, j] = palette[color]
        data[539:541, 959:961] = [255, 0, 0]
        img = toimage(data)       # Create a PIL image
        img.save(f"output/set_1/img{size_b}X{size_a}_"+ str(ratio).replace(".", "-") +f"_{iterations}.png")
        """img.show()"""
        print("Consumed time: ", mktime(gmtime()) - start)

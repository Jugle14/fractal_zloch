from image_creating import toimage, np
from modules import square_loop, convert_speed, jit, convert_speed_2
from time import mktime, gmtime
from values import x as x_centre, y as y_centre

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

    #x_centre = -1
    #y_centre = 0

    x_centre += 0.5 #neeeded action if i want point (0: 0) to be in (0; 0)

    for photo in range(-10,0):
        start = mktime(gmtime())
        print(f"\n\nstarted computing image number {photo}")
        iterations = 8192
        ratio = 2**photo
        # Create a 1024x1024x3 array of 8 bit unsigned integers
        size_a = 1080
        size_b = 1920
        data = np.zeros((size_a, size_b, 3), dtype=np.uint8)

        #data[:,960] = [254,255,255]       # Makes the middle pixel red
        #data[540,:] = [254,255,255]       # Makes the next pixel blue
        
        x_decline = x_centre - 0.5 - 1.5/ratio
        y_decline = y_centre - 2 + 1/ratio
        for i in range(0, size_b):
            for j in range(0, size_a):
                x, y = 3*i/(size_b*ratio) + x_decline, 2 - 2*j/(size_a*ratio) + y_decline    #here could be zoom
                pas, speed = square_loop(iterations, x, y)
                if pas:
                    color = convert_speed_2(speed)
                else:
                    color = convert_speed(speed, iterations)
                data[j, i] = palette[color]
        data[size_a//2-1:size_a//2+1, size_b//2-1:size_b//2+1] = [255, 0, 0]
        img = toimage(data)       # Create a PIL image
        img.save(f"output/testing/img{size_b}X{size_a}_"+ str(ratio).replace(".", "-") +f"_{iterations}_1.png")
        """img.show()"""
        print("Consumed time: ", mktime(gmtime()) - start)

from image_creating import toimage, np
from modules import square_loop, convert_speed, jit
from time import mktime, gmtime

"""@jit(nopython=True)
def main(data, size_a, size_b, iterations):
    for j in range(0, size_b):
        x, y = 2*(i-size_a/2)/size_a, 2*(j-size_b/2)/size_b
        speed = square_loop(iterations, x, y)
        color = convert_speed(speed, iterations)
        data[i, j] = [color, color, color]"""

if __name__ == "__main__":
    start = mktime(gmtime())
    iterations = 767
    # Create a 1024x1024x3 array of 8 bit unsigned integers
    size_a = 1080
    size_b = 1920
    data = np.zeros((size_a, size_b, 3), dtype=np.uint8)

    #data[:,960] = [254,255,255]       # Makes the middle pixel red
    #data[540,:] = [254,255,255]       # Makes the next pixel blue
    for i in range(0, size_a):
        for j in range(0, size_b):
            y, x = 2*(i-size_a/2)/size_a, 2*(j-size_b/2)/size_b    #here could be zoom
            speed = square_loop(iterations, x, y)
            color = convert_speed(speed, iterations)
            data[i, j] = [color, color, color]
    img = toimage(data)       # Create a PIL image
    img.save("output/4.png")
    img.show()
    print("Consumed time: ", mktime(gmtime()) - start)

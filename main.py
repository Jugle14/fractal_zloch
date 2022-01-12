"""from image_creating import toimage, np"""
from PIL import Image, ImageDraw
from modules import square_loop, convert_speed, jit
from timeit import default_timer as timer
from values import x as x_centre, y as y_centre, increasing
from multiprocessing import Pool
from palette import palette

@jit(nopython=True)
def color_creating(i, j, size_a, size_b, ratio, x_decline, y_decline, max_iterations):
    x, y = (3*i*10**increasing)/(size_b*ratio) + x_decline, (2 - 2*j/(size_a*ratio))*10**increasing + y_decline    #here could be zoom
    it = square_loop(max_iterations, x, y)
    #color = convert_speed(it, max_iterations)
    return it

def main(photo):
    # Create a 1024x1024x3 array of 8 bit unsigned integers
    size_a = 1080
    size_b = 1920
    # creating a photo element
    im = Image.new('RGB', (size_b, size_a), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    # measuring time
    start = timer()
    print(f"\nstarted computing image number {photo[0]}")
    max_iterations = 800#int(80*(photo[0]+1)**1.0625)
    ratio = 2**photo[0]


    #data[:,960] = [254,255,255]       # Makes the middle pixel red
    #data[540,:] = [254,255,255]       # Makes the next pixel blue
    x_decline = (-1.5/ratio)*10**increasing
    y_decline = (-2 + 1/ratio)*10**increasing
    x_decline += x_centre
    y_decline += y_centre
    for i in range(0, size_b):
        for j in range(0, size_a):
            it = color_creating(i, j, size_a, size_b, ratio, x_decline, y_decline, max_iterations)
            draw.point([i, j], tuple(palette[int(it*128%1024)]))
    im.convert('RGB').save(f"output/testing/img{size_b}X{size_a}_"+ str(ratio).replace(".", "-") +f"_{max_iterations}_1.png", 'PNG')
    print(f"Computing image number {photo[0]} has taken ", timer()-start, "s.")

if __name__ == "__main__":
    photo_range = []
    for i in range(45, 46):
        photo_range += [[i]]
    print(photo_range)
    with Pool(6) as pool:
        pool.map(main, photo_range)

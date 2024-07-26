import timeit
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import multiprocessing
from sctriangulate.colors import build_custom_continuous_cmap

########################################
################ CONTROL ###############
########################################
coord_re = -0.7402022
coord_im = 0.1570541
region = 0.0005
iterations = 600
number_of_processes=8 # 4 or 8 ONLY
########################################
########################################
########################################

size = int(2000 / number_of_processes)
x_min = coord_re - region
x_max = coord_re + region
y_min = coord_im - region
y_max = coord_im + region

re = np.linspace(x_min, x_max, num=2000)
im = np.linspace(y_min, y_max, num=2000)

def is_complex_number_in_m_set(re,im):
    cn = complex(re, im)
    i = 0
    number = complex(0,0)
    result = complex(0,0)
    while i < iterations:
        number = result
        result = number * number + cn
        if abs(result) > 2:
            return i
        i += 1
    return i 

def calculate_mandelbrot_set(operation_field_matrix):
    to_pos = operation_field_matrix * (size-1) + operation_field_matrix - 1 
    from_pos = to_pos - size + 1
    matrix = np.zeros((size, 2000))
    for y in range(size):
        for x in range(2000):
            matrix[y][x] = is_complex_number_in_m_set(re[x], im[y + from_pos]) 
    return matrix

if __name__ == '__main__':
    image = Image.new(mode="RGB", size=(2000, 2000))

    ### Colormaps
    
    #colormap = build_custom_continuous_cmap([168, 0, 14],[217, 90, 22],[230, 161, 0],[235, 234, 228],[18, 178, 199],[19, 87, 171],[10, 9, 89],[0,0,0]) ## Red-Orange-Yellow-White-Lightblue-MiddleBlue-Darkblue-Black
    #colormap = build_custom_continuous_cmap([168, 0, 14],[213, 213, 222],[0,0,0],[168, 0, 14],[213, 213, 222],[0,0,0],[168, 0, 14],[213, 213, 222],[0,0,0],[168, 0, 14],[213, 213, 222],[0,0,0],[168, 0, 14],[213, 213, 222],[0,0,0],[168, 0, 14],[213, 213, 222],[0,0,0]) ## Red-White-Black
    #colormap = build_custom_continuous_cmap([11, 16, 107],[227, 147, 34],[11, 16, 107],[227, 147, 34],[11, 16, 107],[227, 147, 34],[11, 16, 107],[227, 147, 34],[11, 16, 107],[227, 147, 34],[11, 16, 107],[227, 147, 34]) ## Orange-Blue
    #colormap = build_custom_continuous_cmap([194, 0, 58],[179, 9, 32],[103, 105, 107],[63, 66, 69],[0,0,0]) ## Pink-Red-Gray-DarkGray-Black
    #colormap = build_custom_continuous_cmap([0,0,0],[63, 66, 69],[103, 105, 107],[179, 9, 32],[194, 0, 58]) ## Pink-Red-Gray-DarkGray-Black - Reverse

    #colormap = build_custom_continuous_cmap([35, 117, 79],[38, 150, 126],[42, 156, 173],[42, 110, 173],[4, 17, 43],[43, 23, 82],[181, 84, 191],[99, 12, 64],[0,0,0]) ## MiddleGreen-Green-LightBlue-Blue-NavyBlue-DarkMagenta-Magenta-DarkPink-Black
    
    #colormap = build_custom_continuous_cmap([40, 41, 41],[66, 66, 66],[92, 92, 92],[138, 135, 135],[214, 210, 210],[235, 196, 82],[227, 173, 14],[219, 126, 33],[199, 46, 16],[0,0,0]) ## DarkGray-MiddleGray-Gray-White-Yellow-Orange-Red
    
    #colormap = build_custom_continuous_cmap([0,0,0],[5, 4, 54],[7, 6, 74],[12, 11, 110],[22, 56, 130],[59, 93, 168],[120, 152, 222],[197, 206, 224],[232, 193, 102],[217, 138, 2],[166, 83, 0],[125, 63, 1],[0,0,0]) ## Black-NavyBlue--LightBlue-White-LightOrange-Yellow-DarkOrange-Black


    #colormap = build_custom_continuous_cmap([5, 2, 31],[8, 4, 41],[11, 6, 54],[13, 7, 69],[15, 8, 82],[15, 7, 92],[16, 7, 105],[19, 8, 120],[23, 11, 138],[26, 13, 158],[32, 18, 176],[40, 25, 194],[52, 37, 204],[64, 48, 219],[81, 66, 235],[96, 82, 235],[113, 101, 235],[131, 121, 232],[145, 137, 232],[153, 147, 219],[177, 173, 219],[190, 188, 212],[221, 220, 230],
    #                                        [222, 191, 191],[212, 163, 163],[214, 150, 150],[214, 139, 139],[212, 125, 125],[196, 98, 98],[194, 79, 79],[189, 66, 66],[189, 53, 53],[194, 25, 25],[204, 14, 14],[181, 5, 5],[153, 3, 3],[112, 2, 2],[84, 1, 1],[74, 3, 3],[51, 1, 1],[41, 2, 2],[26, 1, 1]) ## DarkBlue -- White -- DarkRed


    #colormap = build_custom_continuous_cmap([235, 102, 0],[235, 141, 0],[230, 209, 179],[163, 162, 160],[189, 22, 0],[117, 5, 10],[14, 29, 153],[1, 9, 74],[0,0,0]) ## Orange-Yellow-White-Gray-Red-DarkRed-Blue-DarkBlue-Black

    #colormap = build_custom_continuous_cmap([99, 164, 166],[50, 157, 161],[9, 113, 117],[0,0,0],[92, 6, 37],[156, 11, 63],[201, 52, 106],[186, 112, 139],[145, 140, 142]) ## Aqua-Black-Pink-Gray
    
    #colormap = build_custom_continuous_cmap([4, 2, 54],[9, 6, 87],[27, 22, 156],[76, 72, 199],[171, 170, 181],[196, 116, 144],[191, 57, 104],[184, 11, 72],[128, 6, 49],[66, 2, 25]) ## DarkBlue-Blue-Gray-Pink-DarkPink

    #colormap = plt.get_cmap('twilight_shifted') #gist_heat, twilight_shifted
    colors = [colormap(i / (iterations + 1))[:3] for i in range(iterations + 1)]
    colors_rgb = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

    print("### Mandelbrot-Set - Multicore ###")
    print("> Starting calculation...")
    start = timeit.default_timer()
    with multiprocessing.Pool(processes=number_of_processes) as pool:
        results = pool.map(calculate_mandelbrot_set, range(1, number_of_processes+1))

    matrix = np.vstack(results)
    
    for x in range(2000):
        for y in range(2000):
            image.putpixel((x,y), colors_rgb[int(matrix[y][x])])

    enhancer = ImageEnhance.Brightness(image)
    enhancer.enhance(1.3).show()

    stop = timeit.default_timer()
    print('>>> Execution time in sec: ', stop - start)
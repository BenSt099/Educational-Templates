import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import numpy as np
import timeit
from PIL import Image
from PIL import ImageEnhance
import multiprocessing

def calculate_mandelbrot_set(frames):
    zoom = 0.01
    max_iterations = 4000
    coord_re = -0.738
    coord_im = 0.24
    re_min = coord_re - zoom
    re_max = coord_re + zoom
    im_min = coord_im - zoom
    im_max = coord_im + zoom
    for _ in range(frames):
        re_min -= zoom
        re_max += zoom
        im_min -= zoom
        im_max += zoom
        max_iterations = max_iterations + 100
        zoom = zoom + 0.01
    im = Image.effect_mandelbrot((800, 800), (re_min, im_min, re_max, im_max), max_iterations)
    enhancer = ImageEnhance.Brightness(im)
    im2 = enhancer.enhance(1.28)
    return np.rot90(np.array(im2), -1), frames

def main(m_sets, frames):
    pygame.init()
    dimx=800
    dimy=800
    scr = pygame.display.set_mode((dimy,dimx))
    pygame.display.set_caption("Mandelbrot-Set - Zoom")
    scr.fill((0,0,0)) 
    running = True
    i = 0
    while running:
        for event in pygame.event.get():
            # Exit program
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if i < frames:
                    surface = pygame.surfarray.make_surface(m_sets[i])
                    scr.blit(surface, (0, 0))
                    pygame.display.update()
                    i = i+1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = 0
    pygame.quit()  

if __name__ == '__main__':
    print("### Mandelbrot-Set - PyGame - Multicore ###")
    print("> Starting calculation...")
    number_of_frames = 30
    print(">>> Number of frames: ", number_of_frames)
    m_sets = []
    start = timeit.default_timer()
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_mandelbrot_set, range(1, number_of_frames + 1))

    print(">>> Number of CPUs / cores: ", multiprocessing.cpu_count())

    for result in results:
        mandelbrot_image, frame_count = result
        m_sets.insert(frame_count, mandelbrot_image)

    m_sets.reverse()

    stop = timeit.default_timer()
    print('>>> Execution time in sec: ', stop - start)

    print("> Calculation done!")
    print("> Entering Main Loop!")
    main(m_sets, number_of_frames)
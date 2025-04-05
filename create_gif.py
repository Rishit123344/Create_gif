import imageio.v3 as iio
filenames = ['pikachu1.png','pikachu2.png']
image = []
for filename in filenames:
    iio.append(iio.imread(filename))
    iio.imwrite("pikachu.gif",image,duration = 500,loop =0)

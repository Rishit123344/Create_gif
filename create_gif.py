import imageio.v3 as iio
filenames = ['team-pic1.png','team-pic2.png']
image = []
for filename in filenames:
    iio.append(iio.imread(filename))
    iio.imwrite("team.gif",image,duration = 500,loop =0)
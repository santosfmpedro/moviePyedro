
import moviepy.editor as mpy

vcodec =   "libx264"

videoquality = "24"

# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "slow"

title = "E:\coding\github\moviePyedro\movies\intros\intro"
loadtitle = title + '.3gp'
savetitle = title + '.mp4'

# modify these start and end times for your subclips
cuts = [('00:00:00.949', '00:00:01.152'),
        ('00:00:02.328', '00:00:03.077')]

import subprocess

from globalVar import *

image_prefix = f"{g_file_dir}/destination%d.jpg"

ffmpeg_command = f"ffmpeg -r {g_input_rate} -start_number 1 -i ./data/img%d.jpg -c:v libx264 -r {g_output_rate} -pix_fmt yuv420p {g_video_name}"
print(ffmpeg_command)
input("go?")
subprocess.run(ffmpeg_command)

print("done")
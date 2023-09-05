import subprocess

input_rate = "1/5"
output_rate = "30"
video_name = "out.mp4"

ffmpeg_command = f"ffmpeg -r {input_rate} -start_number 1 -i ./data/img%d.jpg -c:v libx264 -r {output_rate} -pix_fmt yuv420p {video_name}"
print(ffmpeg_command)
input("go?")
subprocess.run(ffmpeg_command)

print("done")
from globalVar import *
from read_select_files import *
from filterImages import *


nameL = ["destination1.jpg", "destination13.jpg"]
pred_blurL = ["blur", "blur"]
g_rows = transform_to_rows(nameL, pred_blurL)
filter_files(g_rows, f"{g_file_dir}/time.txt")
print("filter_finish")

select_and_make_video(g_file_dir, g_start_time, g_end_time)
print("video_generated")
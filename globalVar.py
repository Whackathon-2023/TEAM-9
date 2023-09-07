##global variables
from datetime import datetime


g_blur_model = 'model/blur_detect.h5'
g_glare_model = 'model/glare_detect.h5'

g_threshold_blur = 0.9
g_threshold_glare = 0.6

#for the original 
g_original_dir = "./userdata"
#for save the sorted images
g_file_dir = "data2"

g_input_rate = "30"
g_output_rate = "30"
g_video_name = "video.mp4"

g_frame_count_weight = 1

#bad quality images
g_rows = []

# g_start_time = datetime(2022, 1, 30, 0, 0)
# g_end_time = datetime(2022, 2, 2, 12, 20)
g_start_time = datetime(2022, 1, 1, 0, 0)
g_end_time = datetime(2022, 2, 22, 12, 20)


###outputs
buffr_blur = []
score_blur = []
pred_blur = [] #blur status of images 


buffr_glare=[]
pred_glare=[] #glare status 
score_glare=[]

glare_points = []
blur_points = []

name=[]

image_array=[]

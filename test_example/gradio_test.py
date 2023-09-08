
import cv2
import gradio as gr
#pip install MoviePy

#def to_black(image):
#    output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    return output

#interface1 = gr.Interface(fn=to_black, inputs="image", outputs="image")
#interface1.launch()
import moviepy.editor as mp

clip = mp.VideoFileClip("D:\zht\consistency_models场景生成\/result-gif\车辆2.gif")
clip.write_videofile("D:\zht\consistency_models场景生成\/result-gif\车辆2.mp4")
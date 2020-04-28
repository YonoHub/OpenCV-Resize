'''
    OpenCV Resize Block's source code
    Auther: Ahmed Hendawy - YonoHub Developer Advocate
    Date: 23.04.2020
'''
# Vision
import cv2
# Yonoarc Utils
from yonoarc_utils.image import from_ndarray, to_ndarray
from yonoarc_utils.header import set_timestamp

class cv2_resize:
    def on_start(self):
        self.resize_type="resize" if self.get_property("resize_type")==0 else "scale"
        self.interpolation=[cv2.INTER_NEAREST,cv2.INTER_LINEAR,cv2.INTER_AREA,cv2.INTER_CUBIC,cv2.INTER_LANCZOS4]
    
    def on_new_messages(self,messages):
        original_image=to_ndarray(messages['original_image'])
        if self.resize_type == "resize":
            height=self.get_property("height") if not self.get_property("height")==0 else original_image.shape[0]
            width=self.get_property("width") if not self.get_property("width")==0 else original_image.shape[1]
        else:
            height=int(original_image.shape[0]*self.get_property("height")) if not self.get_property("height")==0 else original_image.shape[0]
            width=int(original_image.shape[1]*self.get_property("width")) if not self.get_property("width")==0 else original_image.shape[1]
        dim = (width, height)
        
        resized_image = cv2.resize(original_image, dim, interpolation = self.interpolation[self.get_property("interpolation")])

        self.publish("resized_image",from_ndarray(resized_image,messages['original_image'].header))
        


        

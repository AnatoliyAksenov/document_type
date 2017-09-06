from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import model_from_json
import io

json_file = open('model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model/doc_classification.h5")


def predict(img_path):
    #img_path = "d:\\data\\20170831_225723.jpg"
    print(img_path)

    img = load_img(img_path, target_size=(224, 224))  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    classes = loaded_model.predict(x)
    return classes

if __name__ == '__main__':
    cl = predict('C:\\Users\\AKSENO~1\\AppData\\Local\\Temp\\tmp7fd7_fp5')
    print(cl)

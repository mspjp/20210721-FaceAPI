from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials

def main():

    global face_client

    try:
        # 環境変数の取得
        load_dotenv()
        cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        cog_key = os.getenv('COG_SERVICE_KEY')

        # Face client の認証
        credentials = CognitiveServicesCredentials(cog_key)
        face_client = FaceClient(cog_endpoint, credentials)

        DetectFaces(os.path.join('images','people.jpg'))

    except Exception as ex:
        print(ex)


def DetectFaces(image_file):
    print('Detecting faces in', image_file)

    # 顔の取得
    with open(image_file, mode="rb") as image_data:
        detected_faces = face_client.face.detect_with_stream(image=image_data, return_face_attributes=[FaceAttributeType.glasses])

        if len(detected_faces) > 0:
            print(len(detected_faces), 'faces detected.')

            # アノテーションするための準備
            fig = plt.figure(figsize=(8, 6))
            plt.axis('off')
            image = Image.open(image_file)
            draw = ImageDraw.Draw(image)
            color = 'lightgreen'

            # 各顔の枠を描画
            for face in detected_faces:

                # 顔情報の取得
                print('\nFace ID: {}'.format(face.face_id))
                detected_attributes = face.face_attributes.as_dict()              
                if 'glasses' in detected_attributes:
                    print(' - Glasses:{}'.format(detected_attributes['glasses']))

                # アノテーション
                r = face.face_rectangle # 4つ角の座標を取得
                bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
                draw = ImageDraw.Draw(image)
                draw.rectangle(bounding_box, outline=color, width=5)
                annotation = 'Face ID: {}'.format(face.face_id)
                plt.annotate(annotation,(r.left, r.top), backgroundcolor=color)

            # アノテーションされた画像の保存
            plt.imshow(image)
            outputfile = 'detected_faces.jpg'
            fig.savefig(outputfile)

            print('\nResults saved in', outputfile)
    

if __name__ == "__main__":
    main()
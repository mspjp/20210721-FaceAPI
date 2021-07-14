from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# Import namespaces
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

        person_image = os.path.join('images','personA.jpg')
        CompareFaces(person_image, os.path.join('images','people1.jpg'))                

    except Exception as ex:
        print(ex)


def CompareFaces(image_1, image_2):
    print('Comparing faces in ', image_1, 'and', image_2)

    # image_1 にいる人が image_2 にいるかどうか確認
    with open(image_1, mode="rb") as image_data:
        # image_1 から1人の顔を取得
        image_1_faces = face_client.face.detect_with_stream(image=image_data)
        image_1_face = image_1_faces[0]

        # 顔をハイライトさせる
        fig = plt.figure(figsize=(8, 6))
        plt.axis('off')
        image = Image.open(image_1)
        draw = ImageDraw.Draw(image)
        color = 'lightgreen'
        r = image_1_face.face_rectangle
        bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle(bounding_box, outline=color, width=5)
        plt.imshow(image)
        outputfile = 'face_to_match.jpg'
        fig.savefig(outputfile)

    # image_2 に映っている全員の顔を取得
    with open(image_2, mode="rb") as image_data:
        image_2_faces = face_client.face.detect_with_stream(image=image_data)
        image_2_face_ids = list(map(lambda face: face.face_id, image_2_faces))

        # image_2 の顔の中から、image_1 から取得した顔に似ている顔を取得
        similar_faces = face_client.face.find_similar(face_id=image_1_face.face_id, face_ids=image_2_face_ids)
        similar_face_ids = list(map(lambda face: face.face_id, similar_faces))

        # 描画の準備
        fig = plt.figure(figsize=(8, 6))
        plt.axis('off')
        image = Image.open(image_2)
        draw = ImageDraw.Draw(image)

        # マッチした顔をアノテーション
        for face in image_2_faces:
            if face.face_id in similar_face_ids:
                r = face.face_rectangle
                bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
                draw = ImageDraw.Draw(image)
                draw.rectangle(bounding_box, outline='lightgreen', width=10)
                plt.annotate('Match!',(r.left, r.top + r.height + 15), backgroundcolor='white')

        # アノテーションされた画像の保存
        plt.imshow(image)
        outputfile = 'matched_faces.jpg'
        fig.savefig(outputfile)
    

if __name__ == "__main__":
    main()
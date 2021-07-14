# 20210714-FaceAPI
MS Tech Camp #9


## 環境

- Python 3.6 以降
- Windows / macOS / Linux
- 仮想マシンでも可能

### Python ライブラリのインストール

以下のコマンドで "requirements.txt" に記載の Python ライブラリを一括インストールする。
```
pip install -r requirements.txt
```


## 手順

### 1. Azure ポータルでリソースを作成する

1-1. Cognitive Services を検索し、[作成] をクリックします。

![](https://user-images.githubusercontent.com/39784917/125489210-54a459f5-d036-4a59-a273-9b1829410a16.png)

1-2. 必要事項を記入します。

|項目|記入・設定例|
|--|--|
|サブスクリプション|Azure for Students|
|リソースグループ|rg-mstechcamp9|
|リージョン|東日本|
|名前|cog-mstechcamp9|
|価格レベル|Standard S0|
|契約条件の同意|チェックを入れる|

1-3. 確認と作成をし、完了次第リソースへ移動しておきます。

### 2. Python プログラムの環境構築

2-1. 任意のリポジトリで本リポジトリをクローンし移動します。

```
git clone https://github.com/mspjp/20210721-FaceAPI.git
cd 20210721-FaceAPI/
```

2-2. 本リポジトリ直下に ".env" ファイルを作成し、Azure ポータルで作成した Cognitive Service リソース内、[キーとエンドポイント] を参考に以下を記入します。

**※ ".env" ファイルに記述した値は、リポジトリ固有の環境変数として参照されます。".env" ファイルに記入された Cognitive Service のキーとエンドポイントの値は GitHub などで公開すると他人に悪用される恐れがあるため、".gitignore" ファイルに `.env` と追記することで追跡対象から除外します。（本リポジトリでは既に設定済み）**

```
COG_SERVICE_ENDPOINT=[エンドポイント]
COG_SERVICE_KEY=[キー 1]
```

下記画像の場合、以下のように記入

```
COG_SERVICE_ENDPOINT=https://cog-mstechcamp9.cognitiveservices.azure.com/
COG_SERVICE_KEY=ace0738c04cd4fXXXXXXXXXXX
```

![](https://user-images.githubusercontent.com/39784917/125547763-dff571ad-684d-455f-bfb7-19c766ad1e59.png)

### 3. 顔検出プログラムの実行

3-1. 'detect_faces.py' 実行します。
```
python detect_faces.py
```

以下のような出力が確認できれば成功です。

```
Detecting faces in images/people.jpg
2 faces detected.

Face ID: 4df8b9ed-103f-4c16-9b59-f63e81abd867
 - Glasses:noGlasses

Face ID: 972d7535-cdaa-42b6-900c-206a00a87acb
 - Glasses:readingGlasses

Results saved in detected_faces.jpg
```

3-2. リポジトリ内に 'detected_faces.jpg' というファイルができます。開くと、下記のように顔がアノテーションされており、それぞれ ID が振られていることが分かります。

![](https://user-images.githubusercontent.com/39784917/125585367-fa781a4e-f0f0-45b1-a628-e635ced4f9ca.png)

### 4. 顔情報の取得

他にも様々な要素を取得できます。詳しくは ['FaceAttributes' クラスのドキュメント](https://docs.microsoft.com/ja-jp/dotnet/api/microsoft.azure.cognitiveservices.vision.face.models.faceattributes) の Properties を参照してください。

### 4. 顔比較プログラムの実装

## 参考資料
- [Microsoft Learn | Detect, analyze, and recognize faces](https://docs.microsoft.com/learn/modules/detect-analyze-recognize-faces/)
- [AI-102-AIEngineer | Detect, Analyze, and Recognize Faces](https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/19-face-service.html)
- [Face API ドキュメント](https://docs.microsoft.com/dotnet/api/overview/azure/cognitiveservices/face-readme)

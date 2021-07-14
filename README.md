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

## 概要
画像内での顔の位置や、予測される年齢や性別が得られる。
```JSON
{
  "faces": [
      {
        "age": 32,
        "gender": "Female",
        "faceRectangle": {
          "top": 225,
          "left": 237,
          "width": 130,
          "height": 130
        }
      },
      {
        "age": 29,
        "gender": "Female",
        "faceRectangle": {
          "top": 309,
          "left": 534,
          "width": 119,
          "height": 119
      }
    }
  ]
}
```


## 手順

### 1. Azure でリソースを作成する

1-1 Cognitive Services のリソースを作成

![](https://user-images.githubusercontent.com/39784917/125489210-54a459f5-d036-4a59-a273-9b1829410a16.png)

1-2 必要事項の記入

|項目|記入・設定例|
|--|--|
|サブスクリプション|Azure for Students|
|リソースグループ|rg-mstechcamp9|
|リージョン|東日本|
|名前|cog-mstechcamp9|
|価格レベル|Standard S0|
|契約条件の同意|チェックを入れる|

### 2. Python プログラムの作成

2-1 任意のリポジトリへ移動し、本リポジトリをクローン
```
git clone https://github.com/mspjp/20210721-FaceAPI.git
```

2-2 本リポジトリ直下に ".env" ファイルを作成し、Azure ポータルで作成した Cognitive Service リソース内、[キーとエンドポイント] を参考に以下を記入

※ ".env" ファイルに記述した値は、リポジトリ固有の環境変数として参照されます。".env" ファイルに記入された Cognitive Service のキーとエンドポイントの値は GitHub などで公開すると他人に悪用される恐れがあるため、".gitignore" ファイルに `.env` と追記することで追跡対象から除外します。
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

2-3 "analyze-faces.py" を実行


## 参考資料
- [Detect, analyze, and recognize faces (Microsoft Learn)](https://docs.microsoft.com/learn/modules/detect-analyze-recognize-faces/)
- https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/19-face-service.html


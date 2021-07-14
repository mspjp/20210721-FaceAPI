# 20210714-FaceAPI
MS Tech Camp #9


## 環境

- Python 3.6 以降
- Windows / macOS / Linux
- 仮想マシンでも可能

### Python ライブラリのインストール
```
pip install python-dotenv
pip install pillow
pip install matplotlib
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

2-2 "analyze-faces.py" を実行


## 参考資料
- [Detect, analyze, and recognize faces (Microsoft Learn)](https://docs.microsoft.com/learn/modules/detect-analyze-recognize-faces/)
- https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/19-face-service.html


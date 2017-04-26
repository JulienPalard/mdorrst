# Arrogant（傲慢）

求職資訊的api

_`arrogant`_ 是天主教中七原罪的傲慢之罪<br>
因為系統會幫學生累計他們的實習紀錄等等，當成`胸前的勳章`<br>
期望大家在累積的過程中要小心不要傲慢(好像有點牽強XD)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [API](#api)
  - [parameter](#parameter)
  - [usage and Results](#usage-and-results)
- [Getting Started](#getting-started)
- [Prerequisities](#prerequisities)
- [Installing](#installing)
- [Running & Testing](#running--testing)
- [Run](#run)
  - [Break down into end to end tests](#break-down-into-end-to-end-tests)
  - [And coding style tests](#and-coding-style-tests)
- [Deployment](#deployment)
- [Built With](#built-with)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## API

api domain：目前還沒架起來，所以暫定`127.0.0.1`<br>
請在api domain後面接上正確的url pattern以及query string<br>
詳細的參數以及結果請參閱下面介紹

### parameter

- `school`：餐廳的id
- `dept`：系所。
- `degree`：年級。
- `location`：所在的縣市名稱。
- `start`：如果回傳型態是陣列的話，需要指定回傳陣列的哪個部份（python的slice）。例如回傳使用者的評論時，若指定start=1，則會回傳array[0:15]共15個。
- `id`：該職缺物件的ID

### usage and Results

API使用方式（下面所寫的是api的URL pattern）<br>
Usage of API (pattern written below is URL pattern)：


1. _`get/jvalue`_：  

  - 職缺id
  - example： [http://127.0.0.1:8000/arrogant/get/jvalue?id=754](http://127.0.0.1:8000/arrogant/get/jvalue?id=754)

    ```
    {
      "avatar": "/media/maid_BwdsckP.png",
      "company": "雲雀國際股份有限公司",
      "fromWitchWeb": "1111",
      "id": 754,
      "job": "台南遠百店-涮乃葉 內外場計時人員(實習",
      "url": "http://www.1111.com.tw/job-bank/job-description.asp?eNo=79117525&agent=internships",
      "休假制度": "排休, 輪休",
      "到職日期": "不限",
      "地區": "台南市東區",
      "學歷限制": "不拘",
      "實習時段": "暑期實習、學期實習、學年實習",
      "工作地點": "台南市東區 前鋒路210號四樓(大遠百",
      "工作性質": "兼職、企業實習",
      "工作時間": "日班, 中班, 晚班, 假日班, 輪",
      "工作經驗": "不拘",
      "工作說明": "「涮乃葉」為雲雀在台開幕之新品牌歡迎您加",
      "科系限制": "不拘",
      "聯絡人員": "林店長",
      "職務類別": "餐飲服務人員、餐廚助手",
      "職缺更新": "2017/4/19",
      "薪資": "時薪 133至150",
      "身份類別": "一般求職者／日間就學中",
      "需求人數": "不限"
    }
    ```
    
2. _`get/recommendJvalue`_：取得推荐的實習或求職執缺

  - school
  - dept
  - degree
  - expample： [http://127.0.0.1:8000/arrogant/get/recommendJvalue?school=NCHU&dept=U56&degree=3](http://127.0.0.1:8000/arrogant/get/recommendJvalue?school=NCHU&dept=U56&degree=3)

    ```
    {
      "avatar": "/media/maid_BwdsckP.png",
      "company": "雲雀國際股份有限公司",
      "fromWitchWeb": "1111",
      "id": 754,
      "job": "台南遠百店-涮乃葉 內外場計時人員(實習",
      "url": "http://www.1111.com.tw/job-bank/job-description.asp?eNo=79117525&agent=internships",
      "休假制度": "排休, 輪休",
      "到職日期": "不限",
      "地區": "台南市東區",
      "學歷限制": "不拘",
      "實習時段": "暑期實習、學期實習、學年實習",
      "工作地點": "台南市東區 前鋒路210號四樓(大遠百",
      "工作性質": "兼職、企業實習",
      "工作時間": "日班, 中班, 晚班, 假日班, 輪",
      "工作經驗": "不拘",
      "工作說明": "「涮乃葉」為雲雀在台開幕之新品牌歡迎您加",
      "科系限制": "不拘",
      "聯絡人員": "林店長",
      "職務類別": "餐飲服務人員、餐廚助手",
      "職缺更新": "2017/4/19",
      "薪資": "時薪 133至150",
      "身份類別": "一般求職者／日間就學中",
      "需求人數": "不限"
    }
    ```

3. _`get/jlist`_：取得實習列表

  - location
  - start
  - 範例： [http://127.0.0.1:8000/arrogant/get/jlist?location=台中市南區&start=1](http://127.0.0.1:8000/arrogant/get/jlist?location=台中市南區&start=1)

    ```
    [
      {
        "fields": {
          "avatar": "politician.png",
          "company": 1014,
          "fromWitchWeb": "1111",
          "job": "【探魚】Intern實習生 (台中南區)早班/晚班/假日/工讀/兼職Part Time",
          "url": "http://www.1111.com.tw/job-bank/job-description.asp?eNo=79889630&agent=internships",
          "休假制度": "排休",
          "到職日期": "不限",
          "地區": "台中市南區",
          "學歷限制": "不拘",
          "實習時段": "暑期實習、學期實習、學年實習",
          "工作地點": "台中市南區",
          "工作性質": "兼職、企業實習",
          "工作時間": "日班, 中班, 晚班, 假日班",
          "工作經驗": "不拘",
          "工作說明": "「最有文藝氣息的烤魚店」新店籌備中，熱烈歡迎熱愛美食，喜歡與人互動、正向思考，對品牌經營管理有熱情、有使命感的夥伴加入我們的團隊，與我們一起提供客戶美好的用餐體驗，成就你的夢想，為自己的職涯加分! ! 1.內場區餐點備製、食材/物料及存貨管理等。 2.外場區現場顧客服務(包括顧客接待/帶位、收銀、點餐/供餐、桌邊服務、收盤清理等)、客區清潔與維護。 3.櫃檯區POS點餐操作、營運現金控管、客戶資料庫管理、行銷實務操作等。",
          "科系限制": "不拘",
          "聯絡人員": "營運主管",
          "職務類別": "餐廚助手、餐飲服務人員、其它料理廚師",
          "職缺更新": "2017/4/23",
          "薪資": "面議",
          "身份類別": "日間就學中／夜間就學中",
          "需求人數": "不限"
        },
        "model": "arrogant.job",
        "pk": 795
      }
      ...
      ...
      ...
    ]
    ```


4. _`get/comment`_：取得該實習的使用者留言

  - id
  - start  
  - expample： [http://127.0.0.1:8000/arrogant/get/comment?id=754&start=1](http://127.0.0.1:8000/arrogant/get/comment?id=754&start=1)

    ```
    [
      {
        "fields": {
          "Job": 754,
          "create": "2017-04-24T11:54:42Z",
          "raw": "測試測試"
        },
        "model": "arrogant.comment",
        "pk": 1
      },
      {
        "fields": {
          "Job": 754,
          "create": "2017-04-24T14:13:08.788Z",
          "raw": "這是測試"
        },
        "model": "arrogant.comment",
        "pk": 2
      },
      {
        "fields": {
          "Job": 754,
          "create": "2017-04-24T14:19:11.154Z",
          "raw": "測試第三次XD"
        },
        "model": "arrogant.comment",
        "pk": 3
      }
    ]
    ```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need `python3`

  - Linux：`sudo apt-get update; sudo apt-get install; python3 python3-dev`
  - OSX：`brew install python3`

## Installing

1. `pip install arrogant`

## Running & Testing

## Run

1. `settings.py`裏面需要新增`arrogant`這個app：

  - add this:

    ```
    INSTALLED_APPS=[
    ...
    ...
    ...
    'arrogant',
    ]
    ```

2. `urls.py`需要新增下列代碼 把所有search開頭的request都導向到`arrogant`這個app：

  - add this:

    ```
    import arrogant.urls
    urlpatterns += [
        url(r'^arrogant/',include(arrogant.urls, namespace="arrogant") ),
    ]
    ```

3. `python manage.py runserver`：即可進入頁面測試 `arrogant` 是否安裝成功。

### Break down into end to end tests

目前還沒寫測試...

### And coding style tests

目前沒有coding style tests...

## Deployment

`arrogant` is a django-app, so depends on django project.

## Built With

- djangoApiDec,

## Contributors

- **張泰瑋** [david](https://github.com/david30907d)

## License

This package use `GPL3.0` License.

## Acknowledgments

感謝 `剛之煉金術師`給予命名靈感

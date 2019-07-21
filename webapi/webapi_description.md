# [WebAPIについての説明](https://qiita.com/busyoumono99/items/9b5ffd35dd521bafce47)

## 知識編
### アプリケーションの種類
- スタンドアロン
  - 他の機器に依存せず単独で動作するアプリケーション。
- クライアントサーバ
    ```
    コンピュータをサーバとクライアントに分け役割分担をして運用する仕組みのことです。
    ```
    - 役割が違う別なコンピュータ同士がネットワークで繋がっているアプリケーション。
### クライアントサーバ型の特徴
- クライアントとサーバで役割分担
- クライアント多い、サーバ少ない
- クライアントとサーバはネットワークで接続している
- クライアントとサーバで通信する
- クライアントとサーバの両方を使って1つのアプリ(サービス）を提供する
- データを1つのものとして扱える
### クライアントサーバ型の仕事の流れ
- クライアントから仕事の依頼
- サーバで頑張る
- サーバから結果を返す
- クライアントで結果を受け取って、いい具合に表示する
### サーバとは
英語的にいうと、サービスを提供する人。
クライアントからの依頼を受け取ってサービスを提供するコンピュータやソフト。機能だったりデータだったりする。

前後の文脈でコンピュータ自体のハードだったり、コンピュータ内のソフトだったりするのでややこしい。

- 種類
  - Webサーバ
  - DBサーバ
  - アプリケーションサーバ
  - メールサーバ

### クライアントとは
サーバを利用するコンピュータ等。ユーザとやり取りをしてユーザの代理でサーバに問い合わせをする。

銀行のシステムでいうとATM
インターネットを利用する時のクライアントは主にブラウザ。アプリの場合もあるよ。

### Webブラウジング
Webブラウジングとはインターネットでサイトを見る事
Webブラウジングもクライアントサーバ型。
クライアントであるブラウザがWebサーバにhttpで通信してコンテンツを表示する。

### プロトコルとは
一言でいうと通信の為のルール。ルールが無いと「相手が何言ってるかわかんない」ってなる。
プロトコルの種類としてはIPとかFTPとかがある。

### http(プロトコル)とは
英語的にいうと、HyperText Transfer Protocolの略。HyperTextはhtml(HyperText Markup Language)の事と思えば良い。

単にhttpという時と、httpプロトコルっていう時がある。
```
インターネット上でWebサーバー（サイトの公開側）と、クライアント（ブラウザ：サイトを閲覧する側）が、相互に通信するために使用される仕組みです。

もっと言うと、Webサーバーとクライアント間で、HTML（Webページを作成するための言語）で記載された情報をやりとりするための仕組みです。
```
### httpのポイント
大きく分けてリクエストとレスポンスがある。
日本語でいうと要求と反応。
#### リクエスト(要求)
別な言い方をすると注文。クライアントからサーバに送る。
よくあるのはデータが欲しいとか、データを保存してとかをリクエストする
以下リクエストの中身。

- URL
- メソッド
  - GET：サーバへデータの要求
  - POST：サーバへデータを送る
  - 他にもPUT、DELETEとかあるよ

#### レスポンス(反応)
別な言い方をすると結果。リクエスト受けたサーバがクライアントに返す。
リクエストされたデータの中身とか、登録した結果など。
以下レスポンスの中身。

- ステータスコード（成否とかを数字で表現している）
  - 200：成功
  - 400：リクエストが不正
  - 500：サーバのエラー
- コンテンツ(html)

### Webのブラウジングの流れ
またの名をここまでのまとめ。
ブラウジングはクライアント(ブラウザ)とサーバがhttpという決まりで通信してコンテンツ(html)を出力する。

レストランで例えるなら

役割
|レストラン	| ブラウジング|
| --- | --- |
| ウエイター | クライアント|
| コック | サーバー |
| 伝票と料理 | http|

流れ
| レストラン | ブラウジング|
| --- | --- | 
| お客さんが店に入店する |ブラウザを開く|
| お客さんが、ウエイターに注文する | urlの入力|
| ウエイターは伝票に記入してコックに渡す | リクエスト|
|コックは料理を作る | サーバ処理|
|コックは伝票と料理をウエイターに渡す | レスポンス|
|ウエイターはお客さんに伝票と料理を提供| コンテンツの表示|

#### レストランで例えた説明の詳細1
**コックのスタンス**
- コックはウエイターがどういう方法で注文を受け付けたのかは気にしない。 お店にお客さん来て注文、電話注文、FAX注文、ネット注文何でも良い。とにかく伝票クレというスタンス。
- ブラウジングでいうと、サーバはクライアントが何かは気にしない。PCのブラウザでもスマホアプリでも何でも良い。

#### レストランで例えた説明の詳細2
ウエイターのスタンス
- ウエイターはコックがどう料理するかは気にしない。コックが1人で作ってる。コックが1000人で作ってる。スイーツは隣のお店から買っている、とか別に興味が無い。とにかく伝票と料理をクレというスタンス。
- ブラウジングでいうと、クライアントはサーバがどういう処理しているかは気にしない。DBがMysqlでもOracleでもよいし、ハードウェア的に1台のコンピュータでも複数台のコンピュータでもよいし、サーバから別なサーバを参照しててもよい。

#### レストランで例えた説明の詳細3
伝票
- 伝票はお客さんの注文が書いてある。実際のレストランではありえないけど、ウエイターに対して、伝票を料理と一緒に渡す時にこの注文が「成功したよ」とか「失敗したよ」とかを伝票に書いて渡すイメージ。口で説明しないで伝票に書くルールになっているイメージ。
- ブラウジングでいうと、ユーザーが指定したサイトのデータをくれとhttpの中に含めてサーバにリクエストを送る。サーバは成功(又は失敗)したよっていう情報とサイトの中身であるhtmlを返す。失敗の時は基本的にはhtmlは空で返す

#### レストランで例えた説明の詳細4
ステータスコード：404
いちばん有名なステータスコードではなかろうか。

- レストランなのに、お客さんがウエイターに車を注文する。ウエイターは律儀にコックさんへその伝票を渡す。コックさんは「そんなのない」って返す時のステータスコード。
- ブラウジングでいうと、ユーザーが指定したURLが、間違っていた・今はもうなくなった等で対応するサイトが無い時
ステータスコードが400番台の場合はリクエストが不正という意味になっている。

#### レストランで例えた説明の詳細5
ステータスコード：500
- お客さんがウエイターに注文する。ウエイターはコックさんへその伝票を渡す。コックさんはキッチンが壊れている等の理由で仕事出来ない。そんな時に返すステータスコード。
- ブラウジングでいうと、サーバがハード的に壊れたとかソフトにバグがあるとかに出る。
ステータスコードが500番台の場合はサーバ側に問題あるという意味になっている。
エンジニアはこれが出ると対応に追われる

#### レストランで例えた説明の詳細6
ステータスコード：200
- お客さんがウエイターに注文する。ウエイターはコックさんへその伝票を渡す。コックさんは料理をつくる。「美味しく出来たぞ！」って時に返すステータスコード。
- ブラウジングでいうと、正常にサイトが表示できた時
ステータスコードが200番台の場合は正常であるという意味になっている。
一般の方々が目にすることは無い。

### APIとは
簡単な例えでいうと、プログラムの関数のようなもの。

詳しく
```
APIは「Application Program Interface」の略で簡単に説明すると、どのアプリーケーションでも共通で使える機能を提供する仕組みです。
```

更に詳しく
```
APIは「Application Programming Interface」の略です。アプリケーションプログラミングインターフェイス。
　例えば「AというファイルをBという名前でコピーをして、作業完了したら、ポップアップウィンドウを出して知らせる！」というプログラムを作るとします。実際にどんな動きをするのかパートに分けてみると……、

1. Aというファイルを選択
2. 実行ボタンを押すと3のステップへ
3. データをコピーする
4. コピーされたデータをBという名前を付け保存
5. ポップアップウィンドウを出して作業完了を告げる
　この1.〜5.の作業をすべて一から作成すると、かなり手間が掛かります（マウスの動きを計算して、ウィンドウのデザインを考えて……）。そこで登場するのがAPIです。

1. ファイルを選択するAPI
2. ボタンを押すとプログラムを動かすAPI
3. データをコピーするAPI
4. ファイルに名前を付けるAPI
5. ウィンドウを出してメッセージを出すAPI
と、いろいろな機能があるAPIから、必要なAPIを探し出し組み合わせるだけで、プログラムができてしまうのです。つまりAPIは「特定の機能を持つプログラム部品」なのです。よく使われる命令をAPIにしてみんなで共有してしまえば、非常に効率的に作業ができますね。
```

### WebAPIとは
ネットワーク越しに利用できる関数。URLが関数名で引数を渡す事で結果が変化する。

以下外部のより詳しい説明。
簡単にいうと
(APIに)Webサービスを付与したものがWeb APIとなります。

詳しく
コンピュータプログラムの提供する機能を外部の別のプログラムから呼び出して利用するための手順・規約(API：Application Programming Interface)の類型の一つで、HTTPなどWebの技術を用いて構築されたもののこと。
Webサイトに外部のサイトの提供する機能や情報を組み込んだり、アプリケーションソフトからWeb上で公開されている機能や情報を利用する際などに用いられる。
Web APIで機能を公開しているサーバに対して、インターネットなどの通信ネットワークを通じて依頼内容をHTTPリクエストの形で送信すると、処理結果がHTTPレスポンスの形で送られてくる。送受信されるデータの形式はAPIによって様々だが、Webでよく用いられるXMLやHTML、JSON、各種の画像ファイル形式などが用いられることが多い。

### WebAPIとブラウジング
WebAPIもhttpの通信でリクエストしてレスポンスを貰う。
ブラウジングと流れは一緒。

### WebAPIの一旦のまとめ
- サーバーで用意している関数(機能)をhttpで通信して利用する事。
- 利用するには決め事を守ってリクエストを出す。
- 決まり事とはURLとか渡すデータの名前とかデータの形式とか。
- レスポンスは大体何かしらのデータ。時々画像も。
- データの形式は最近はJSON。一昔前はXMLが主流だった。
- ajax形式で利用される事が多い

### JSONとは
データを簡単に表現する仕組み。
#### JSONのサンプル
chromeのデベロッパーツール>コンソールで以下をコピペして試してみる。

JSONのJS上での例
```
// 定義
var data = {
    name : 'kobayashi',
    age : 24,
    schols : [
        '千葉小学校',
        '神奈川中学校',
        '東京高校'
        ]
};

// 利用
console.log(data.name);
console.log(data.age);
console.log(data.schols);
console.log(data.schols[0]);
```

### JSON定義のポイント
- keyとvalueがセットになっている
- valueの種類には文字列、数値、配列、連想配列(オブジェクト)がある
- 文字列
  - シングルクォート(')かダブルクォート(”)で囲む
- 数字
  - そのまま打ち込む。(何かで囲む必要は無い)
- 配列
  - []で囲む
  - keyが数字で省略できる。というか省略する。
  - 利用する時には0から始まる
- 連想配列(オブジェクト)
  - {}で囲む
  - keyが文字
  - keyとvalueの区切りはコロン(:)
- 配列、連想配列(オブジェクト)共通
  - key,valuセットの区切りはカンマ(,)
  - カンマ最後に付けるとエラーになる

### JSON利用のポイント
連想配列(オブジェクト)の場合は変数名.keyでvalueを使う。
配列は変数名.key[0]のように数字をカギカッコで囲んで利用する。

### ajaxとは
「Asynchronous JavaScript ＋ XML」の略で、javascriptを使って非同期にDOM(htmlタグの事でdivタグ、imgタグ等の事)を操作したり、データを取得する実装の方法の1つ。
ajax的アプローチの一部で、WebAPIから都度必要になったデータを取得する事が含まれる。
Googleマップで有名になった。

### 非同期とは
処理の種類の事で、同期と非同期がある。

同期は処理が直列的に順次実行する処理方法の事。途中に別な処理の依頼があっても後回しにする。
非同期は処理が並列的に同時に実行(される事もある)する処理方法の事。

ブラウジングでの同期的処理はページのリロードにあたる。リロードをするとレスポンスが返ってくるまで他の操作は出来ない。
非同期的な処理はリロードせずに内容を変更したり、他の操作が継続して出来ること。


## 実践編
### WebAPIの流れ
- クライアントから
- httpで
- リクエストして
- サーバー処理して
- レスポンスが返ってくる
大事な事なので何回も言いました。 

### 自前で作る時に事前に決める事
- URLはどうする。通常データは名詞にする。
- リクエストデータの構成。
  - keyとvalue
- レスポンスデータの構成
  - JSONかXMLか
  - keyとvalue
- エラー時のレスポンス
  - レスポンスデータ内で表現するか
  - httpステータスコードで表現するか
リクエスト、レスポンス共に何のデータが必要で、直感的に分かりやすいデータ構成かどうかで決めます。
また、今後の変更に対して柔軟に対応出来るかどうかも考えて決めます。

以下API設計のフロー
例えば郵便番号APIで言えば

- URLどうする？
  - zipcloud.ibsnet.co.jp/api/addressでもよくね？
  - 今後の仕様変更に備えてzipcloud.ibsnet.co.jp/api/v1/searchのようにバージョン挟む？
- リクエストデータどうする？
  - 1つで7桁数値で貰う？250と0011の2つに分けて貰う？
  - 1つだとしてkeyはzipとか、codeとかzip_codeとかでもよくね？
- レスポンスデータどうする？
  - address1じゃなくてprefにする？
といった感じで検討する

### WebAPI(サーバ)-要件定義例
- ユーザリストの一覧
- phpで作る。
- 簡略化の為にDBは使用しない。
- 簡略化の為に入力値(引数に当たるもの)の検証はしない
- ユーザには管理者、オペレーター、ゲストのユーザタイプがある。
- ユーザタイプ毎のデータを返す。
- データはJSON形式

### WebAPIを作る-作成フロー
パターンがあるよ
前置きとして、データを返す場合のWebAPIの場合の大まかな流れはほぼ一緒でパターンとして以下のようになるよ。

- リクエストと一緒に渡されたデータを取得
- リクエストデータの検証とか解析
- レスポンスデータの値を作成
  - ここではユーザ一覧
  - 通常はDBの操作(検索、追加、変更、削除)
- レスポンスデータの作成
  - 場合によってはレスポンスデータの検証
  - 検索結果0件の場合とか
  - 変更が正しく行われなかったとか...
- JSON形式でレスポンスを返す。
特にリクエストの検証の部分は、有名なSQLインジェクション(DBを削除出来る攻撃)を防ぐ意味でも必要です。

また、ログインが必須のアプリケーションなら先頭にログインチェックが入ります。

### WebAPIの調査
自分でWebAPIを作って無いなら、まずWebAPIの仕様を調べる。WebAPI(PHP)を作った人に聞くか、仕様書を読むなりして以下の内容を確認する。
- URLは？
- 何のデータをどうやって渡すか
  - keyは？
  - valueの形式や中身は
- 何のデータがどんな形で返ってくるか
  - jsonの形式の場合
  - keyは
  - valueの形式や中身は
  - 一昔前はresultを付けて返す事が多かった。

ファイルの読み方
- URL
  - ファイルの設置場所とファイル名。
- リクエストデータのkey
  - $_REQUEST,$_POST,$_GETの中に入ってる
  - $_REQUEST['user_type']の場合、keyはuser_type
- リクエストデータのvalue
  - リクエストデータの検証している部分から推測
- レスポンスデータのkey,value
  - JSON形式ならjson_encode()関数に渡してる値がレスポンスデータの中身。その前の処理を読んで- key,valueを確認
- エラー時のレスポンス方法
  - header("HTTP/1.1 400 Bad Reques");とかあればhttpステータスコード使ってる
  - phpファイルでは無く、クライアント側のデベロッパーツールとかで確認
但しフレームワークとか使ってる場合は、上記にあてはまらない事が多い。別途フレームワークの勉強しよう。頑張ろう。

### jQueryでWebAPIを利用する。
今回はクリックイベントが発生した時にWebAPIを叩くように作成する。別にクリックイベント以外のreadイベントでも良い。
クライアントからWebAPIへリクエスト出すには、jQueryのajax()関数を使用する。(他にも別な関数あるが今回は触れない)

大きな流れとしては以下のようになる。

- リクエストの下準備
- リクエストの実行
- レスポンスの判定
- レスポンスデータの利用

ajax()内にリクエスト部分とレスポンス部分がある。
-url,dataType,dataはリクエスト
- success,errorはレスポンス

リクエスト
- urlは文字列で
- dataは文字列、数字、JSON形式のどれかで書く

レスポンス処理
レスポンスのhttpステータスコードによって処理が変わる

| ステータスコード | 実行される処理 |
| --- | --- | 
|200番代	       | success|
|400,500番代	   | error|

それぞれ処理を書く。
通常successでもerrorでもhtmlを操作してエンドユーザにお知らせする。

今回のサンプルでは成功時,失敗時ともdiv[data-result]に内容を表示している

### デバッグの方法
問題あっても無くてもデバッグして確認する。
特に問題が無いように見えているだけの時があるから注意する。

chromのDev toolで何が起こっているか確認できる。

Network:通信の状態をリアルタイムで確認。
Console:自分で仕込んだログを表示。

意図しない動作やエラーがあれば都度修正してデバッグする。

まとめ
- httpの仕組みを利用していて、リクエストとレスポンスがある
- それはブラウジングもWebAPIも同じ
- データを返すWebAPIを作成する時はパターンがある
- WebAPIを使う前に調査する。用意するもの、返ってくるもの
- jQuery.ajax()でリクエストとレスポンス処理を書ける
- デバッグしながら完成させる


# [0からREST APIについて調べてみた](https://qiita.com/masato44gm/items/dffb8281536ad321fb08)
## REST APIの概要
### REST APIとは
```
RESTful API(REST API)とは、Webシステムを外部から利用するためのプログラムの呼び出し規約(API)の種類の一つで、RESTと呼ばれる設計原則に従って策定されたもの。RESTそのものは適用範囲の広い抽象的なモデルだが、一般的にはRESTの考え方をWeb APIに適用したものをRESTful APIと呼んでいる。

RESTful APIでは、URL/URIですべてのリソースを一意に識別し、セッション管理や状態管理などを行わない(ステートレス)。同じURLに対する呼び出しには常に同じ結果が返されることが期待される。

また、リソースの操作はHTTPメソッドによって指定(取得ならGETメソッド、書き込みならPOSTメソッド)され、結果はXMLやHTML、JSONなどで返される。また、処理結果はHTTPステータスコードで通知するという原則が含まれることもある。
```
### RESTとは
REpresentational State Transferの略

RESTの4つの設計原則
  - セッションなどの状態管理を行わない。(やり取りされる情報はそれ自体で完結して解釈することができる)
  - 情報を操作する命令の体系が予め定義・共有されている。（HTTPのGETやPOSTメソッドなど）
  - すべての情報は汎用的な構文で一意に識別される。（URLやURIなど）
  - 情報の内部に、別の情報や(その情報の別の)状態へのリンクを含めることができる。
リソースに対してURLが対応づけられる。（そのため、URLが名詞的になることが多い）

### RESTなAPIとそうではないAPIの例
そうではないAPI
- URLに各機能のパスが紐付いている

RestなAPI
- リソースに基づいてURLが決まる
- ユーザー情報等の対応付を作り送られたリソースに応じて処理を行う
- 送られるリソースの種類(作成・取得・更新・削除についてはHTTPの一般的なリクエストメソッドを使用)
  - GET
    - 取得
  - POST
    - 作成
  - PUT
    - 更新
  - DELETE
    - 削除

### メリット・デメリット
#### メリット
アプリケーションの中のリソースがURIで示せる。
　アドレス欄に入力すれば、そのリソースを参照できる。
　- どのリソースを操作しようとしているかがわかる。

URIに規則が生まれることで、利用する開発者が楽になる。
　- 将来想定されるシステム規模の増大に対応可能な設計である。

ステートレスにすることで、スケーラビリティが向上。
　- アクセスの集中に耐えやすい構造にできる。

統合の相対的な容易さ
　- 標準的なデータフォーマット(XMLやJSON)を扱うことで、
　　他システムとの連携が容易になる。
　- RESTに基づいたWebアプリでは、インタフェースが固定されている為
　　互換性の問題が発生しない。

標準的なAPIの提供
　RESTfulAPIを公開することで、
　標準的なデータフォーマットを使い、多様なアプリケーションを提供することができる。

```
※URI
URI はUniform Resource Locator (URL) の考え方を拡張したものである。 
URI は http/https や ftp などのスキームで始まり、コロン (:) による区切りのあとに
スキームごとに定義された書式によってリソースを示す。

引用：Uniform Resource Identifier - ウィキペディア
https://ja.wikipedia.org/wiki/Uniform_Resource_Identifier
```

#### デメリット
・RESTの制約
　- プログラミング言語はリソース指向ではないので、URIとマッピングするコードは汚くなりがち

　REST APIをハイパーテキスト駆動にするのは比較的難しい。

### REST APIはどう使われる？
どう使われるのか？
RESTは状態を持たないという特性から
SNSなど多くのアクセスが考慮されるサービスのAPIに向いている。

また、シンプルな設計とすることができるので、
サービスを作る際にAPIが必要になったという場合でも
その部分はRESTの設計を検討してみるとよいかもしれない。

# [翻訳: WebAPI 設計のベストプラクティス](https://qiita.com/mserizawa/items/b833e407d89abd21ee72)

## API 設計の勘所
ネット上で目にする API 設計に関する議論は、少しアカデミックすぎたり、個々人の曖昧な主張が入り混じっていて、とても現実世界で通用するものではありません。私はこの記事を通して、実用的かつモダンな API 設計について説明しようと思います。誤解を防いだり、理解を早めていただくために、まずは私が思う API の勘所をお伝えします。

- できる限り Web の標準に従うこと
- 開発者に親切な作りにすること。また、ブラウザのアドレスバーから叩けるようにすること
- シンプルで一貫性を持たせ、直感的かつ心地よく使えるようにすること
- Enchant（本体のサービス）が提供する機能を十分に活用できるものにすること
- 様々な要件とのバランスを保ちつつ、効率的に開発ができるようにすること
API は開発者のための UI です。他の UI と同じように、UX にもとことんこだわりましょう！

## RESTful な URL にしよう
REST のキーとなる概念は、論理的に分割されたリソースを HTTP メソッド（GET, POST, PUT, PATCH, DELETE）で操作する、ということです。

「リソースを論理的に分割する」
- API 利用者が客観的に見て意味がわかる名詞（動詞じゃありません！）を使って分割する

REST の原則に従うと、HTTP メソッドを使った CRUD 操作は以下のように定義されます。
- GET /tickets - チケットのリストを取得する
- GET /tickets/12 - 指定したチケットの情報を取得する
- POST /tickets - 新しいチケットを作成する
- PUT /tickets/12 - チケット #12 を更新する
- PATCH /tickets/12 - チケット #12 を部分的に更新する
- DELETE /tickets/12 - チケット #12 を削除する
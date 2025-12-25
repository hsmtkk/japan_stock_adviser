# 構成銘柄一覧

以下Webページから構成銘柄のTickerシンボル、銘柄名を取得する。

日経連続増配株指数
https://indexes.nikkei.co.jp/nkave/index/component?idx=nkcdg

日経累進高配当株指数
https://indexes.nikkei.co.jp/nkave/index/component?idx=nkphd

# 銘柄情報

銘柄情報(株価、PER、PBRなど)を調べるには、以下のコマンドを実行する。

```shell
uv run stock_data symbol
```

(例)トヨタ(Tickerシンボル 7203)の銘柄情報を得る。
```shell
uv run stock_data 7203
```

このコマンドはPythonスクリプト(yfinanceライブラリを使用)を実行し、銘柄情報を得る。

# 株主優待

株主優待を調べるには、以下のコマンドを実行する。

```shell
uv run owner_benefit symbol
```

(例)トヨタ(Tickerシンボル 7203)の株主優待を得る。
```shell
uv run owner_benefit 7203
```

このコマンドはPythonスクリプトを実行し、株探サイトをスクレイピングし、株主優待を得る。

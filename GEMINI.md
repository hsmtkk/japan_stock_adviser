# 構成銘柄一覧

構成銘柄一覧を得るには、以下のコマンドを実行する。

```shell
uv run nikkei_list_symbols idx
```

idxは以下の通りである。
- 日経平均高配当株50指数: nk225hdy
- 日経連続増配株指数: nkcdg
- 日経累進高配当株指数: nkphd
- 日経平均株主還元株40指数: nk225shr

(例)日経平均高配当株50指数の構成銘柄一覧を得る。

```shell
uv run nikkei_list_symbols nk225hdy
```

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

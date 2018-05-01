# MozDir

## Install

Python3とmakeコマンドが使える状態なら

```
$ make install
```

のみ。無ければ

```
$ brew install python3
$ python3 setup.py install --user
```

を実行する。

## Usage

```
$ mozdir FOLDER NUMBER [-c | --cut] [-n | --name <file>] [-h | --help]
```

- FOLDERには基本lessonを入れるとlesson990がコピーされていきます。
- NUMBERには分ける数を、コメントを削除した状態にしたい場合は-cまたは--cutオプション
- sketch_editor.jsではない名前のときは-nまたは--nameオプションの後にたとえばmain_editor.jsならmainを渡してあげます。

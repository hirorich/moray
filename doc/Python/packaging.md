# Pythonプロジェクトをパッケージ化する方法
このチュートリアルでは、シンプルなPythonプロジェクトをパッケージ化する方法を説明します。パッケージを作成するために必要なファイルと構造を追加する方法、パッケージをビルドする方法、そしてPython Package Indexにアップロードする方法を示します。

> このチュートリアルのコマンドの実行に問題がある場合は、コマンドとその出力をコピーしてから、GitHubの [packaging-problems](https://github.com/pypa/packaging-problems) リポジトリの[問題を開いてください](https://github.com/pypa/packaging-problems/issues/new?template=packaging_tutorial.yml&title=Trouble+with+the+packaging+tutorial&guide=https://packaging.python.org/tutorials/packaging-projects)。全力でサポートいたします。

いくつかのコマンドは、より新しいバージョンのpipを必要とするので、まずは最新のバージョンがインストールされていることを確認してください。
```
python -m pip install --upgrade pip
```

***
## シンプルなプロジェクト
このチュートリアルでは、 `example_package` というシンプルなプロジェクトを使用します。自分のプロジェクトをパッケージ化する前に、このプロジェクトを使ってそのままこのチュートリアルに従うことをお勧めします。

次のようなファイル構造をローカルに作成します。
```
packaging_tutorial/
└── src/
    └── example_package/
        ├── __init__.py
        └── example.py
```
`__init__.py` は、ディレクトリをパッケージとしてインポートするために必要なもので、空にしておきます。

`example.py` は、パッケージ内のモジュールの例で、パッケージのロジック（関数、クラス、定数など）を入れることができます。そのファイルを開き、以下の内容を入力します。
``` python
def add_one(number):
    return number + 1
```
Pythonの[モジュール](https://packaging.python.org/glossary/#term-Module)や[インポートパッケージ](https://packaging.python.org/glossary/#term-Import-Package)に慣れていない方は、[Pythonのパッケージとモジュールのドキュメント](https://docs.python.org/ja/3/tutorial/modules.html#packages)に数分目を通してください。

この構造を作成したら、このチュートリアルのすべてのコマンドを `packaging_tutorial` ディレクトリ内で実行することになります。

***
## パッケージファイルの作成
これから、プロジェクトを配布するための準備に必要なファイルを追加していきます。この作業が終わると、プロジェクトの構造は次のようになります。
```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

***
## テスト用ディレクトリの作成
`tests/` は、テストファイル用のプレースホルダーです。とりあえず空にしておきましょう。

***
## pyproject.toml の作成
`pyproject.toml` は、ビルドツール（[pip](https://packaging.python.org/key_projects/#pip) や [build](https://packaging.python.org/key_projects/#build) など）に、プロジェクトのビルドに必要な情報を伝えます。このチュートリアルでは [setuptools](https://packaging.python.org/key_projects/#setuptools) を使用しているので、 `pyproject.toml` を開き、以下の内容を入力します。
``` toml
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
```
`build-system.requires` は、あなたのパッケージをビルドするために必要なパッケージのリストを与えます。ここに何かを列挙すると、インストール後ではなく、ビルド時にのみ利用できるようになります。

`build-system.build-backend` は、ビルドの実行に使用される Python オブジェクトの名前です。[flit](https://packaging.python.org/key_projects/#flit) や [poetry](https://packaging.python.org/key_projects/#poetry) などの別のビルドシステムを使用する場合は、ここに記述し、設定の詳細は以下で説明する [setuptools](https://packaging.python.org/key_projects/#setuptools) の設定とは全く異なります。

背景と詳細については [PEP 517](https://www.python.org/dev/peps/pep-0517/) と [PEP 518](https://www.python.org/dev/peps/pep-0518/) を参照してください。

***
## メタデータの設定
メタデータには、静的と動的の2種類があります。
- 静的メタデータ（`setup.cfg`）：毎回同じであることが保証されています。この方がシンプルで読みやすく、エンコーディングエラーなどの一般的なエラーを回避できます。
- 動的メタデータ（`setup.py`）：非決定性の可能性があります。動的なものやインストール時に決定されるもの、拡張モジュールやsetuptoolsの拡張機能などは、 `setup.py` に入れる必要があります。

静的メタデータ(`setup.cfg`)の方が望ましいです。動的メタデータ (`setup.py`) は、絶対に必要な場合のエスケープハッチとしてのみ使用すべきです。 `setup.py` は以前は必須でしたが、新しいバージョンの setuptools や pip では省略できます。

> ToDo: 静的メタデータ例とオプションの説明

> ToDo: 動的メタデータ例とオプションの説明

ここで紹介したもの以外にもたくさんあります。詳しくは、[プロジェクトのパッケージ化と配布](https://packaging.python.org/guides/distributing-packages-using-setuptools/)をご覧ください。

***
## README.mdの作成
`README.md` を開き、以下の内容を入力します。必要に応じてカスタマイズしてください。
``` md
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
```
私たちの設定では、 `README.md` を読み込んで `long_description` を提供しているため、[ソース配布物を生成](https://packaging.python.org/tutorials/packaging-projects/#generating-archives)する際には、 `README.md` をコードと一緒に含める必要があります。新しいバージョンの [setuptools](https://packaging.python.org/key_projects/#setuptools) は自動的にこれを行います。

***
## LICENSEの作成
Python Package Indexにアップロードされる全てのパッケージには、ライセンスを含めることが重要です。これは、あなたのパッケージをインストールしたユーザに、あなたのパッケージを使用するための条件を伝えるものです。ライセンスの選択については、https://choosealicense.com/ を参照してください。ライセンスを選択したら、 `LICENSE` を開いてライセンステキストを入力します。例えば、MITライセンスを選択した場合、次のようになります。
```
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

***
## 他のファイルを含める
上記のファイルは、あなたの[ソース配布物](https://packaging.python.org/glossary/#term-Source-Distribution-or-sdist)に自動的に含まれます。明示的に含めるファイルをコントロールしたい場合は、 [MANIFEST.in を使ってソース配布物にファイルを含める](https://packaging.python.org/guides/using-manifest-in/#using-manifest-in)を参照してください。

最終的に[ビルドされた配布物](https://packaging.python.org/glossary/#term-Built-Distribution)には、発見された、またはリストされたPythonパッケージに含まれるPythonファイルが含まれます。データファイルを追加するなど、ここに入れるものを制御したい場合は、 [setuptools docs](https://setuptools.pypa.io/en/latest/index.html) の[データファイルの含め方](https://setuptools.pypa.io/en/latest/userguide/datafiles.html)を参照してください。

***
## 配布物・アーカイブの生成
次のステップでは、パッケージの[配布パッケージ](https://packaging.python.org/glossary/#term-Distribution-Package)を生成します。これは、 Python Package Index にアップロードされ、 [pip](https://packaging.python.org/key_projects/#pip) でインストールできるようにするためのアーカイブです。

PyPAの最新版の[ビルド](https://packaging.python.org/key_projects/#build)がインストールされていることを確認してください。
```
python -m pip install --upgrade build
```
> これらのインストールに問題がある場合は、チュートリアルの [Installing Packages](https://packaging.python.org/tutorials/installing-packages/) をご覧ください。

次に、 `pyproject.toml` が置かれているのと同じディレクトリで、このコマンドを実行します。
```
python -m build
```
このコマンドは、大量のテキストを出力し、完了すると `dist` ディレクトリに2つのファイルを生成します。
```
dist/
  example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
```
`tar.gz` ファイルは[ソースアーカイブ](https://packaging.python.org/glossary/#term-Source-Archive)で、 `.whl` ファイルは[ビルド済み配布物](https://packaging.python.org/glossary/#term-Built-Distribution)です。新しい [pip](https://packaging.python.org/key_projects/#pip) のバージョンでは、ビルド済み配布物を優先的にインストールしますが、必要に応じてソースアーカイブにフォールバックします。常にソースアーカイブをアップロードし、プロジェクトが対応するプラットフォーム用のビルド済みアーカイブを提供する必要があります。今回の例では、私たちのサンプルパッケージはどのプラットフォームのPythonとも互換性があるので、必要なビルド済み配布物は1つだけです。

***
## 配布用アーカイブのアップロード
いよいよ自分のパッケージをPythonパッケージインデックスにアップロードする時が来ました。

これは、テストや実験のために用意されたパッケージインデックスの別のインスタンスです。このチュートリアルのように、実際のインデックスに必ずしもアップロードしたくない場合には最適です。アカウントを登録するには、https://test.pypi.org/account/register/ にアクセスして、そのページの手順に従ってください。また、パッケージをアップロードする前に、メールアドレスの確認が必要になります。詳細については、 [TestPyPIの使用方法](https://packaging.python.org/guides/using-testpypi/)を参照してください。

プロジェクトを安全にアップロードするには、 [PyPI API トークン](https://test.pypi.org/help/#apitoken)が必要です。https://test.pypi.org/manage/account/#api-tokens で作成し、"Scope" を "Entire account" に設定します。**トークンをコピーして保存するまで、このページを閉じないでください。**

登録が完了したら、 [twine](https://packaging.python.org/key_projects/#twine) を使って配布パッケージをアップロードすることができます。そのためにはTwineをインストールする必要があります。
```
python -m pip install --upgrade twine
```
インストールが完了したら、Twineを起動して、 `dist` 以下のすべてのアーカイブをアップロードします。
```
python -m twine upload --repository testpypi dist/*
```
ユーザー名とパスワードの入力を求められます。ユーザー名には `__token__` を使用します。パスワードには、 `pypi-` のプレフィックスを含むトークンの値を使用します。

コマンドが完了すると、以下のような出力が表示されます。
```
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: [your username]
Enter your password:
Uploading example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
Uploading example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]
```
アップロードされたパッケージはTestPyPI上で見ることができます。例えば、https://test.pypi.org/project/example-pkg-YOUR-USERNAME-HERE のようになります。

***
## 新しくアップロードしたパッケージのインストール
[pip](https://packaging.python.org/key_projects/#pip) を使ってパッケージをインストールし、動作を確認することができます。[仮想環境](https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments)を作成し、TestPyPIからパッケージをインストールします。
```
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
```
パッケージ名にあなたのユーザー名を必ず指定してください。

pipはTestPyPIからパッケージをインストールし、出力は以下のようになるはずです。
```
Collecting example-pkg-YOUR-USERNAME-HERE
  Downloading https://test-files.pythonhosted.org/packages/.../example-pkg-YOUR-USERNAME-HERE-0.0.1-py3-none-any.whl
Installing collected packages: example-pkg-YOUR-USERNAME-HERE
Successfully installed example-pkg-YOUR-USERNAME-HERE-0.0.1
```
> この例では、 `--index-url` フラグを使用して、ライブの PyPI の代わりに TestPyPI を指定しています。さらに、 `--no-deps` を指定しています。TestPyPIはライブのPyPIと同じパッケージを持っていないので、依存関係をインストールしようとすると失敗したり、予期しないものをインストールしたりする可能性があります。今回のサンプルパッケージには依存関係はありませんが、TestPyPIを使用する際には依存関係をインストールしないようにするのが良い方法です。

パッケージをインポートすることで、正しくインストールされたかどうかをテストできます。仮想環境にいることを確認し、Pythonを実行してください。
```
python
```
そしてパッケージをインポートします。
```
>>> from example_package import example
>>> example.add_one(2)
3
```
`setup.cfg` や `setup.py` で[配布パッケージ](https://packaging.python.org/glossary/#term-Distribution-Package)にどのような `name` を付けたかに関わらず、[インポートパッケージ](https://packaging.python.org/glossary/#term-Import-Package)は `example_package` になっていることに注意してください（この場合、 `example-pkg-YOUR-USERNAME-HERE`）。

***
## Next steps
**おめでとうございます！Pythonプロジェクトのパッケージ化と配布が完了しました。**

このチュートリアルでは、Test PyPI にパッケージをアップロードする方法を紹介しましたが、これは恒久的な保存場所ではないことを覚えておいてください。Testシステムでは、パッケージやアカウントが削除されることがあります。このチュートリアルのようなテストや実験にはTestPyPIを使うのがベストです。

実際のパッケージをPythonパッケージインデックスにアップロードする準備ができたら、このチュートリアルで行ったこととほとんど同じことができますが、以下の重要な違いがあります。
- パッケージには、記憶に残るユニークな名前をつけましょう。チュートリアルで行ったように、ユーザー名を付ける必要はありません。
- https://pypi.org にアカウントを登録してください。これらは2つの独立したサーバーであり、テストサーバーのログイン情報はメインサーバーと共有されないことに注意してください。
- `twine upload dist/*` を使ってパッケージをアップロードし、本物のPyPIで登録したアカウントの認証情報を入力します。本番環境でパッケージをアップロードしているので、`--repository` を指定する必要はありません。パッケージはデフォルトで https://pypi.org/ にアップロードされます。
- `python3 -m pip install [your-package]` を使って、本物の PyPI からパッケージをインストールします。

この時点で、Pythonライブラリのパッケージ化についてもっと知りたいと思ったら、以下のようなことができます。
- [setuptools](https://packaging.python.org/key_projects/#setuptools) を使用したライブラリのパッケージ化については、[プロジェクトのパッケージ化と配布](https://packaging.python.org/guides/distributing-packages-using-setuptools/)を参照してください。
- [バイナリ拡張のパッケージ化](https://packaging.python.org/guides/packaging-binary-extensions/)についてもお読みください。
- [flit](https://packaging.python.org/key_projects/#flit) 、 [hatch](https://packaging.python.org/key_projects/#hatch) 、 [poetry](https://packaging.python.org/key_projects/#poetry) など、 [setuptools](https://packaging.python.org/key_projects/#setuptools) の代替手段を検討してください。

***
## 翻訳元ページ
[Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- コマンドはWindows側を記載
- `py` コマンドは `venv` で環境切り替えたあとの `python` コマンドに変更

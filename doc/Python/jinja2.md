# jinja2
- 高速で表現力豊かな拡張可能なテンプレート・エンジン

***
## 目次
- [ざっくりとした概要](#ざっくりとした概要)
- [サンプルコード](#サンプルコード)
- [API仕様](#api仕様)
  - [PackageLoader](#packageloader)
  - [Environment](#environment)
  - [Template](#template)
- [参考](#参考)

***
## ざっくりとした概要
- 高速で表現力豊かな拡張可能なテンプレート・エンジン
- テンプレート内の特別なプレースホルダーにより、Pythonの構文に似たコードを書くことが可能
- テンプレートにデータを渡して、最終的なドキュメントをレンダリングする

***
## サンプルコード
``` python
from jinja2 import PackageLoader, Environment

def func(param1, param2):
    
    # package 直下の template フォルダからファイルをロードする準備
    loader = PackageLoader(package_name='package', package_path='template')
    
    # ローダーで設定したフォルダ直下の js_template.js をテンプレートとして読み込む
    template = Environment(loader=loader).get_template(name='js_template.js')
    
    # テンプレート内のパラメータを使用して自動生成
    return template.render(param1=param1, param2=param2)
```

***
## API仕様
### [PackageLoader](https://jinja.palletsprojects.com/en/3.0.x/api/?highlight=packageloader#jinja2.PackageLoader)
- Pythonパッケージ内のディレクトリからテンプレートを読み込む
- ディレクトリとしてインストールされたパッケージのみサポート

### [Environment](https://jinja.palletsprojects.com/en/3.0.x/api/?highlight=environment#jinja2.Environment)
- Jinjaの中核となるコンポーネント
- get_template
  - loaderを使って名前でテンプレートを読み込み、Templateを返す
  - テンプレートが存在しない場合は、TemplateNotFoundが発生

### [Template](https://jinja.palletsprojects.com/en/3.0.x/api/?highlight=environment#jinja2.Template)
- Environment からコンパイルされたテンプレートを表す
- render
  - テンプレート内のパラメータを使用して生成した str を返す

***
## 参考
- [jinja2](https://jinja.palletsprojects.com/en/3.0.x/)

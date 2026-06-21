# Calculator — シンプルな四則演算計算機

Python で書かれた、足し算・引き算・掛け算・割り算ができる計算機です。  
プログラミング初心者でも読みやすいシンプルな構造になっています。

---

## ファイル構成

```
my first project/
├── calculator.py   # 計算機の本体（Calculator クラス）
└── README.md       # このファイル
```

---

## 使い方

### 1. スクリプトとして直接実行する

```bash
python calculator.py
```

実行すると、以下のような結果が表示されます。

```
足し算 10 + 5 = 15
引き算 10 - 5 = 5
掛け算 10 * 5 = 50
割り算 10 / 5 = 2.0
```

### 2. 別のスクリプトから読み込んで使う

```python
from calculator import Calculator

calc = Calculator()

print(calc.add(3, 7))        # 10
print(calc.subtract(10, 4))  # 6
print(calc.multiply(6, 7))   # 42
print(calc.divide(15, 3))    # 5.0
```

---

## メソッド一覧

| メソッド | 説明 | 例 |
|---|---|---|
| `add(a, b)` | 足し算 | `add(3, 4)` → `7` |
| `subtract(a, b)` | 引き算（a − b） | `subtract(10, 3)` → `7` |
| `multiply(a, b)` | 掛け算 | `multiply(3, 4)` → `12` |
| `divide(a, b)` | 割り算（a ÷ b） | `divide(10, 4)` → `2.5` |

> **注意：** `divide` で `b = 0` を渡すと `ValueError` が発生します。

---

## 動作環境

- Python 3.8 以上
- 外部ライブラリは不要です

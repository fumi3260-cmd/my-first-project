"""
calculator.py — 四則演算を行うシンプルな計算機モジュール

このモジュールは Calculator クラスを提供します。
足し算・引き算・掛け算・割り算の4つの計算ができます。
"""


class Calculator:
    """シンプルな四則演算計算機クラス。

    足し算・引き算・掛け算・割り算の4種類の計算メソッドを持ちます。

    使い方の例::

        calc = Calculator()
        result = calc.add(3, 5)   # → 8
        result = calc.divide(10, 2)  # → 5.0
    """

    def add(self, a, b):
        """2つの数を足し算します。

        Args:
            a (int | float): 1つ目の数
            b (int | float): 2つ目の数

        Returns:
            int | float: a と b の合計

        Example:
            >>> calc = Calculator()
            >>> calc.add(3, 4)
            7
        """
        return a + b

    def subtract(self, a, b):
        """2つの数を引き算します（a から b を引く）。

        Args:
            a (int | float): 引かれる数
            b (int | float): 引く数

        Returns:
            int | float: a から b を引いた結果

        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10, 4)
            6
        """
        return a - b

    def multiply(self, a, b):
        """2つの数を掛け算します。

        Args:
            a (int | float): 1つ目の数
            b (int | float): 2つ目の数

        Returns:
            int | float: a と b の積

        Example:
            >>> calc = Calculator()
            >>> calc.multiply(3, 4)
            12
        """
        return a * b

    def divide(self, a, b):
        """2つの数を割り算します（a を b で割る）。

        Args:
            a (int | float): 割られる数（分子）
            b (int | float): 割る数（分母）。0 は指定できません。

        Returns:
            float: a を b で割った結果

        Raises:
            ValueError: b が 0 のとき（ゼロ除算は許可されていません）

        Example:
            >>> calc = Calculator()
            >>> calc.divide(10, 4)
            2.5
        """
        if b == 0:
            raise ValueError("0で割ることはできません")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("足し算 10 + 5 =", calc.add(10, 5))
    print("引き算 10 - 5 =", calc.subtract(10, 5))
    print("掛け算 10 * 5 =", calc.multiply(10, 5))
    print("割り算 10 / 5 =", calc.divide(10, 5))

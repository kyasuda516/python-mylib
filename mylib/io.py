# Copyright (c) 2023 Kanta Yasuda (GitHub: @kyasuda516)
# This software is released under the MIT License, see LICENSE.

import typing as __typing
from pathlib import Path as __Path

def yes_no_input(message: str) -> bool:
  """ユーザーにはい/いいえの質問を表示し、それに対する回答を返す。

  Args:
    message (str): ユーザーに表示するメッセージ。

  Returns:
    bool: ユーザーが "yes" を入力した場合は True、"no" を入力した場合は False を返す。
  """

  while True:
    choice = input(f"{message} ([y]/N): ").lower()
    if choice in ('y', 'ye', 'yes'):
      return True
    elif choice in ('n', 'no'):
      return False

def num_input(message: str, start: int, stop: int) -> int:
  """ユーザーに数字の選択肢を提示し、その範囲内の整数を返す。

  Args:
    message (str): ユーザーに表示するメッセージ。
    start (int): 範囲内の最小値（含む）。
    stop (int): 範囲内の最大値（含まない）。

  Returns:
    int: 範囲内の整数。
  """

  print(message)
  nums = list(range(start, stop))
  while True:
    choice = input(f'Prease choose from {start} to {stop-1}: ')
    try:
      num = int(choice)
      if num in nums:
        return num
    except:
      pass

def num_input2(question: str, options: __typing.Union[list, dict], opt_prefix: str='', opt_suffix: str='') -> __typing.Any:
  """ユーザーに選択肢の入力を促し、リストの値、または辞書のキーに対応する値を返す。

  Args:
    question (str): 入力を促すためのメッセージ。
    options (list | dict): 選択肢のリストまたは辞書。
    opt_prefix (str, optional): 各選択肢の名前の前に表示する文字列。デフォルトは空文字列。
    opt_suffix (str, optional): 各選択肢の名前の後に表示する文字列。デフォルトは空文字列。

  Returns:
    Any: 選択された選択肢のキーに対応する値。
  """

  keys = None
  options_type = type(options).__name__

  if options_type == 'list':
    keys = list(range(len(options)))
  elif options_type == 'dict':
    keys = list(options.keys())
  else:
    raise TypeError("argument 'options' must be list or dict.")
  
  msg = question
  for idx, key in enumerate(keys):
    msg = f'{msg}\n{idx: 3}\t{opt_prefix}{options[key]}{opt_suffix}'
  idx = num_input(msg, 0, len(keys))
  
  if options_type == 'list':
    value = options[idx]
    return value
  elif options_type == 'dict':
    key = keys[idx]
    return key


def blank_ng_input(message: str) -> str:
  """ユーザーに対して、入力を求める。この関数は、入力が空の場合に再試行を求める。

  Args:
    message (str): 入力を求めるときに表示されるメッセージ。

  Returns:
    str: ユーザーが入力した文字列。

  Raises:
    TypeError: 入力された値が文字列型ではない場合。
  """

  while True:
    choice = input(message).strip()
    if choice != '':
      return choice

def fpath_existing_input(message: str, ext: str=None) -> __Path:
  """存在するファイルパスをユーザーに入力させる。

  Args:
    message (str): 入力を求めるときに表示されるメッセージ。
    ext (str, optional): ファイルパスの拡張子。デフォルトはNone。

  Returns:
    pathlib.Path: 入力されたファイルパスに対応するPathオブジェクト。

  Raises:
    FileNotFoundError: 入力されたファイルパスが存在しない場合。
    TypeError: 入力された値が文字列型ではない場合。
  """

  while True:
    p = __Path(input(message).strip().replace('"', ''))
    if (ext is None or p.suffix==ext) and p.exists():
      return p

class Outputter():
  """テキストファイルに文字列を出力するためのクラス。

  Args:
    txt_path (pathlib.Path): 出力先テキストファイルのパス。

  Attributes:
    txt_path (pathlib.Path): 出力先テキストファイルのパス。
  """

  from pathlib import Path as __Path
  def __init__(self, txt_path: __Path, encoding: str='UTF-8'):
    """Outputterクラスのコンストラクタ。引数で指定されたパスのテキストファイルを作成する。

    Args:
      txt_path (pathlib.Path): 出力先テキストファイルのパス。
    """

    self.txt_path = txt_path
    self.encoding = encoding
    with open(self.txt_path.as_posix(), 'w', encoding=self.encoding) as f:
      f.write('')
  
  def output(self, msg: str):
    """テキストファイルに文字列を追記する。

    Args:
      msg (str): 出力する文字列。

    Returns:
      None
    """

    with open(self.txt_path.as_posix(), 'a', encoding=self.encoding) as f:
      f.write(msg)

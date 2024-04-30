if __name__ == "__main__":
  # Introduction to Python iterables

  for index in range(3):
    print(index)

  str = "Iterables"
  for ch in str:
    print(ch)

  ranks = ["high", "medium", "low"]
  for rank in ranks:
    print(rank)

  # What is an iterator

  colors = ["red", "green", "blue"]
  print(colors)

  iter_colors = iter(colors)
  print(iter_colors)

  color = next(iter_colors)
  print(color)

  color = next(iter_colors)
  print(color)

  color = next(iter_colors)
  print(color)

  # color = next(iter_colors)
  # StopIteration

  colors = ["red", "green", "blue"]
  iter_colors = iter(colors)
  for color in iter_colors:
    print(color)

import sys

N = int(sys.stdin.readline())

for i in range(1, 2 * N):
  star = ""
  for k in range(N):
    if (N - k > abs(N - i)):
      star += "*"
    else:
      star += " "

  arrayStar = list(star)
  arrayStar.reverse()
  reverseStar = "".join(arrayStar)

  print(star+reverseStar)

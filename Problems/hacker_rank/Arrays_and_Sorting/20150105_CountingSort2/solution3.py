def counting_sort(ar):
  counts = [0] * len(ar)
  for a in ar:
    counts[a] += 1
  res = []
  for i, c in enumerate(counts):
    if 0 < c:
      res.extend([i] * c)
  return res

  
if __name__ == '__main__':
  n = int(input())
  ar = list(map(int, input().split()))
  print(" ".join([str(r) for r in counting_sort(ar)]))

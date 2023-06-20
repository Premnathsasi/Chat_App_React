def maxSe(sentences):
  max_index=0
  max_count=0
  for i, sentence in enumerate(sentences):
    count = sentence.count('a')
    if count > max_count:
      max_count = count
      max_index = i
  return max_index
sentences = ["ananya loves sharpener", "apple is a very healthy fruit", "this is great thanks very much"]
print(maxSe(sentences))
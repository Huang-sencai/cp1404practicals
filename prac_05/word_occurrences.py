texts=str(input("Text:")).split()
word_to_count={}
for text in texts:
    word_to_count[text]=word_to_count.get(text,0)+1
max_len=max(len(text) for text in word_to_count)
for text in sorted(word_to_count):
    print(f"{text:{max_len}} : {word_to_count[text]}")
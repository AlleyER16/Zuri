text = input("Enter a text/sentence: ")

#removes extra white spaces
text = text.strip()

if text == "": 
    print(f"Word count: {0}")
else:
    text = text.split(" ")

    print(f"Word count: {len(text)}")
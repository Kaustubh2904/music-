from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


string = ""
with open('lyrics.txt', 'r') as file:
    # Read all lines from the file into a list
    lines = file.readlines()

# Print the content of the file
for line in lines:
    # print(line.strip())  # Strip removes the newline character at the end
    string = string + " " + line.strip()

print(summarizer(string, max_length=50, min_length=5, do_sample=False))


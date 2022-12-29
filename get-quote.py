import random

def main():
  # Read the lines from the quotes file and store them in a list
  with open("quotes.txt") as f:
    quotes = f.readlines()

  # Select a random quote from the list
  quote = random.choice(quotes)

  # Print the quote
  print(quote)

if __name__== "__main__":
  main()
  
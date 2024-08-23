def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
    return clean_text
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")

print(snake_case("User Name 187"))
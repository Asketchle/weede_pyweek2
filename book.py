# Novel Series Timeline Tracker
print("=== Novel Series Timeline Tracker ===\n")

# Book Information
book_title = input("Enter book title: ")
in_series = input("Is this book part of a series? (yes/no): ").lower()
is_series = in_series == "yes"

if is_series:
    series_name = input("Enter series name: ")
    book_number = int(input("Enter book number in series: "))
    is_prequel = input("Is this a prequel? (yes/no): ").lower()
    prequel_status = is_prequel == "yes"
    total_books = int(input("Total books in series so far: "))
    books_read = int(input("How many books have you read: "))
else:
    print("Standalone book noted.")

# Availability Check
pdf_available = input("Is PDF version available online? (yes/no): ").lower()
has_pdf = pdf_available == "yes"
audio_available = input("Is audio version available online? (yes/no): ").lower()
has_audio = audio_available == "yes"

# Story Elements
main_character = input("Main character name: ")
is_side_story = input("Is this a side story/spin-off? (yes/no): ").lower()
side_story = is_side_story == "yes"

if side_story:
    side_character = input("Which side character is this story about: ")
    last_appearance = int(input(f"How many books ago did {side_character} last appear: "))
    if last_appearance == 0:
        print(f"{side_character} is currently in the main series!")
    elif last_appearance == 1:
        print(f"{side_character} was just in the previous book")
    elif last_appearance > 5:
        print(f"{side_character} hasn't appeared in {last_appearance} books - long absence!")
    else:
        print(f"{side_character} last appeared {last_appearance} books ago")

new_characters = input("Are there new important characters? (yes/no): ").lower()
has_new_characters = new_characters == "yes"

if has_new_characters:
    num_new_characters = int(input("How many new important characters: "))
    if num_new_characters == 1:
        new_char_name = input("Enter new character name: ")
        print(f"New character '{new_char_name}' added!")
    elif num_new_characters > 1:
        print(f"Adding {num_new_characters} new characters:")
        new_char_names = input("Enter their names (separated by commas): ")
        print(f"New characters added: {new_char_names}")
    else:
        print("No new characters to add.")
else:
    print("No new characters in this book.")

# Character tracking
returning_character = input("Does a character return after absence? (yes/no): ").lower()
has_returning = returning_character == "yes"

if has_returning:
    return_char_name = input("Which character is returning: ")
    books_absent = int(input(f"How many books has {return_char_name} been absent: "))
    if books_absent <= 1:
        print(f"{return_char_name} was only gone briefly")
    elif books_absent >= 5:
        print(f"MAJOR RETURN! {return_char_name} has been gone for {books_absent} books!")
    else:
        print(f"{return_char_name} returns after {books_absent} books")

setting = input("Main setting/location: ")
key_item = input("Important item/object: ")
theme = input("Main theme: ")

# Display book info
if is_series:
    if prequel_status:
        print(f"\n--- {book_title} (Prequel to {series_name}) ---")
        print("Reading order: Read this BEFORE the main series")
    elif book_number == 1:
        print(f"\n--- {book_title} ({series_name} - Book {book_number}) ---")
        print("Reading order: START HERE")
    elif book_number > books_read:
        print(f"\n--- {book_title} ({series_name} - Book {book_number}) ---")
        print("Reading order: NOT YET READ - Coming up next!")
    else:
        print(f"\n--- {book_title} ({series_name} - Book {book_number}) ---")
        print("Reading order: COMPLETED")
else:
    print(f"\n--- {book_title} (Standalone) ---")

# Availability Status
print(f"\n--- Availability ---")
if has_pdf and has_audio:
    print("Available in: PDF and Audio formats")
    print("Status: Both formats accessible online!")
elif has_pdf and not has_audio:
    print("Available in: PDF only")
    print("Status: Audio version not available")
elif has_audio and not has_pdf:
    print("Available in: Audio only")
    print("Status: PDF version not available")
else:
    print("Available in: Neither format online")
    print("Status: Check library or purchase physical copy")

# Display story elements
print(f"\n--- Story Elements ---")
print(f"Main Character: {main_character}")

if side_story:
    print(f"\n*** SIDE STORY SPOTLIGHT ***")
    print(f"Featured Character: {side_character}")
    print(f"Story Type: Spin-off novel for side character")
    if last_appearance == 0:
        print(f"Status: Active in main series")
    elif last_appearance >= 3:
        print(f"Status: Been away from main series for {last_appearance} books")
    else:
        print(f"Status: Recent main series appearance")

if has_new_characters:
    if num_new_characters == 1:
        print(f"New Character: {new_char_name}")
    elif num_new_characters > 1:
        print(f"New Characters ({num_new_characters}): {new_char_names}")
    print("Character development: Expanding cast!")
elif not has_new_characters:
    print("New Characters: None")
    print("Character development: Focusing on existing characters")

if has_returning:
    print(f"\n*** CHARACTER RETURN ***")
    print(f"Returning Character: {return_char_name}")
    print(f"Absence Duration: {books_absent} books")
    if books_absent >= 5:
        print("Impact: MAJOR storyline reunion!")
    elif books_absent <= 2:
        print("Impact: Brief absence, smooth return")
    else:
        print("Impact: Moderate absence, significant return")

print(f"\nLocation: {setting}")
print(f"Key Item: {key_item}")
print(f"Theme: {theme}")

# Series Progress (only if part of series)
if is_series:
    percent_complete = (books_read / total_books) * 100
    has_finished = books_read >= total_books
    
    print(f"\n--- Series Progress ---")
    print(f"Books read: {books_read}/{total_books}")
    print(f"Progress: {percent_complete:.1f}%")
    print(f"Series complete: {has_finished}")
    
    if books_read < total_books:
        books_left = total_books - books_read
        print(f"Books remaining: {books_left}")
        if books_left == 1:
            print("Almost done! Just one more book!")
        elif books_left <= 3:
            print("You're close to finishing!")
    elif books_read == total_books:
        print("Congratulations! Series complete!")
    else:
        print("You've read more than the current series!")

file_names = "book_cover.jpg cover.png Book_cover.jpg illustration.jpg ILLUSTRATION.JPG my_cover.png photo.gif award.jpg Award.jpg award.JPG"

files = file_names.split()
jpg_files = [file.lower() for file in files if file.lower().endswith('.jpg')]

res = sorted(set(jpg_files))

print(' '.join(res))

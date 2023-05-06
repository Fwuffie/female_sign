# ♀️ Esolang

This is a esolang designed entirely to make this t-shirt technically compilable, to add an extra level of irony.
![T-Shirt Image says i.{code} like a girl(); // Try To Keep Up](/t-shirt.jpg "T-Shirt")

This esolang compiles to python. To use run `python3 {source_file} {out_file}` I refuse to put effort into this so it has to be run for every file.

## Key Changes
1. Comments using JS notation are now acceptable "//" They are removed during compile.
2. Lines Ending in a semi-colon now have a use. By placing them at the end of lines they will cause spaces in that line to be ignored.
3. class variables can be executed as a param-less function by wrapping the variable in {} i.e. class.{helloworld} => class.helloworld()
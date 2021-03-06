These are some utilities I have written.

## trackPackage

`trackPackage.py` prints the latest update about a package you're expecting in the mail. It is intended for occasional personal use on your computer.

## xorTable

`xorTable.py` generates the pretty image I use for my avatar on github. Each pixel is the XOR of its x and y coordinates. It can also print out a table of `x XOR y` or it can apply a XOR cellular automata rule to a random sequence of points to generate an image.

## photoMover
`photoMover.py` is for moving all files with a given extension from a directory to destination/YYYY/MM/DD/. By default is moves ./IMG_YYYYMMDD*.jpg from the current working directory to ~/Pictures/YYYY/MM/DD/, but it has flags to let you move a variety of other files:
- `-e` - move files with this extension. Default is "jpg"
- `-b` - regex for the initial part of the filename. Default is "IMG_"
- `[source]` - default is current working directory
- `[destination]` - default is ~/Pictures

## mandelbrot
`mandelbrot.py` tries to guess whether a complex number is in the mandelbrot set or not.

## humanshuffle
`humanshuffle.py` shuffles a list in a way that appears random to humans. Humans will complain if `[1, 2, 3, 4]` shuffles to `[1, 3, 2, 4]` because it's "not random enough". This function is useful for when the appearance of randomness is more important than actual randomness. For example when deciding what order a group of players should take their turns in, people will be happier if the order is considerably different than last time.
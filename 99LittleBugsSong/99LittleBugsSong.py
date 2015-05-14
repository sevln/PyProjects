# 99 LITTLE BUGS SONG
# Prints out every to line to the "99 Little Bugs" Song when executed

for i in range(99, 0, -1):

    if i == 1:
        print("%d little bug in the code.\n%d little bug." % (i, i))
        print("Take it down, patch it around.\nNow there are no more bugs in the code!")
    else:
        print("%d little bugs in the code.\n%d little bugs." % (i, i))
        print("Take one down, patch it around.\n%d little bugs in the code.\n" % (i - 1))



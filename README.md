# Sabbath
Check how much you work on weekends. 

Script assumes that Monday-Friday are working days and Saturday + Sunday are weekend. It is up to us to interpret the results.

## Usage
```
$ git log --date=short | grep "^Date:" | sabbath.py -s -c
$ git log --date=short --since="2013-01-01" | grep "^Date:" | sabbath.py -s

$ git log --date=short --author=Erkal | grep "^Date:" | sabbath.py -5
$ echo $?
```

## Samples

[<img src="http://www.binarni.net/projects/sabbath/remember_the_sabbath.png">](http://www.binarni.net/projects/sabbath/remember_the_sabbath.png)

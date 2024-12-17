For those who may want to use this, keep in mind that the script currently does not convert the full output from the spectrum window into a filter curve file.
You do you have remove the first line where it says "Frequency (Hz)	Level (dB)", and make sure that there is only 1 tab character separating the numbers.
The script will print the output to the console, so run this script in the command line. Also, the output is a single line string, so no newlines. This is because the filter curve file doesn't seem to work if each point is on a different line.
So you would just copy that entire output into a new .txt file, but format the file like this:

FilterCurve: <the script output goes here>
FilterLength="8191" InterpolateLin="1" InterpolationMethod="B-spline"

Again, all off the point data has to go all on one line.

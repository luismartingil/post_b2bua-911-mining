#
#
# Generating the graphs associated with the
# mining of the 911 calls.
# 
# gnuplot <name_of_this_file>
#
# luismartingil - 2013
# http://www.luismartingil.com
#
#

reset

my_font = "Helveltica, 14"
my_big_font = "Helveltica, 20"
my_line_width = "2"
my_axis_width = "1.5"
my_ps = "1.2"

# set default point size
set pointsize my_ps

red_000 = "#F9B7B0"
red_025 = "#F97A6D"
red_050 = "#E62B17"
red_075 = "#8F463F"
red_100 = "#6D0D03"

blue_000 = "#A9BDE6"
blue_025 = "#7297E6"
blue_050 = "#1D4599"
blue_075 = "#2F3F60"
blue_100 = "#031A49" 

green_000 = "#A6EBB5"
green_025 = "#67EB84"
green_050 = "#11AD34"
green_075 = "#2F6C3D"
green_100 = "#025214"

brown_000 = "#F9E0B0"
brown_025 = "#F9C96D"
brown_050 = "#E69F17"
brown_075 = "#8F743F"
brown_100 = "#6D4903"

grid_color = "#ccaabb"
text_color = "#6a6a6a"

set style line 1 linecolor rgbcolor blue_025 linewidth my_line_width pt 7
set style line 2 linecolor rgbcolor green_025 linewidth my_line_width pt 5
set style line 3 linecolor rgbcolor red_025 linewidth my_line_width pt 9
set style line 4 linecolor rgbcolor brown_025 linewidth my_line_width pt 13
set style line 5 linecolor rgbcolor blue_050 linewidth my_line_width pt 11
set style line 6 linecolor rgbcolor green_050 linewidth my_line_width pt 7
set style line 7 linecolor rgbcolor red_050 linewidth my_line_width pt 5
set style line 8 linecolor rgbcolor brown_050 linewidth my_line_width pt 9
set style line 9 linecolor rgbcolor blue_075 linewidth my_line_width pt 13
set style line 10 linecolor rgbcolor green_075 linewidth my_line_width pt 11
set style line 11 linecolor rgbcolor red_075 linewidth my_line_width pt 7
set style line 12 linecolor rgbcolor brown_075 linewidth my_line_width pt 5
set style line 13 linecolor rgbcolor blue_100 linewidth my_line_width pt 9
set style line 14 linecolor rgbcolor green_100 linewidth my_line_width pt 13
set style line 15 linecolor rgbcolor red_100 linewidth my_line_width pt 11
set style line 16 linecolor rgbcolor brown_100 linewidth my_line_width pt 7
set style line 17 linecolor rgbcolor "#224499" linewidth my_line_width pt 5

# this is to use the user-defined styles we just defined.
set style increment user

# set the color and font of the text of the axis
set xtics textcolor rgb text_color font my_font
set ytics textcolor rgb text_color font my_font
set ztics textcolor rgb text_color font my_font

# set the color and font (and a default text) for the title and each axis
set title "Top Title" textcolor rgb text_color font my_big_font
set xlabel "X Label (unit)" textcolor rgb text_color font my_font
set ylabel "Y Label (unit)" textcolor rgb text_color font my_font
set zlabel "Z Label (unit)" textcolor rgb text_color font my_font 

# set the text color and font for the label
set label textcolor rgb text_color font my_font

# set the color and width of the axis border
set border 31 lw my_axis_width lc rgb text_color

set key outside box width 2 height 2 enhanced spacing 2

# set grid color
set grid lc rgb grid_color

# set terminal postscript landscape
set term pngcairo size 720,480 enhanced font "Helvetica,20"
#set term postscript

# Generating graph
unset key
# set size 1.2,1
set output "../img/dayow.png"
set title "2. Calls for the given days of the week"
set xlabel "Day of the week"
set ylabel "Calls"
set xtics font "Helveltica, 16" nomirror
plot 'b2bua/dayow.csv' using 2:xticlabels(1) with linespoints title ''
unset output

# Generating graph
unset key
set output "../img/hourod.png"
# set size 1.2,1
set title "3. Calls for the given hours of the day"
set xlabel "Hour of the day"
set ylabel "Calls"
set xtics font "Helveltica, 12" nomirror rotate by -45
plot 'b2bua/hourod.csv' using 2:xticlabels(1) smooth bezier with lines
unset output

# Generating graph
unset key
set output "../img/eday.png"
# set size 1.8,1
set title "1. Overall days"
set xlabel "Date (Sep 1st 2013 - Jan 1st 2014)"
set ylabel "Calls"
set xtics font "Helveltica, 14" nomirror rotate by -45
set xdata time
set timefmt "%m/%d/%y"
set format x "%m/%d"
plot 'b2bua/eday.csv' using 1:2 with linespoints title ''
unset output
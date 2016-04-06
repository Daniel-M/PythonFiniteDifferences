set terminal gif animate
set output "heatmap.gif"
set view map
set dgrid3d
set pm3d interpolate 10,10
set cbrange[0:1]
set palette rgb 21,22,23 # Set heat map palette as "hot"
do for [i=1:10000:1]{
	#splot sprintf("iteration.%d",i) using 1:2:3 with pm3d
	splot sprintf("results/iteration.%d",i) using 1:2:3 with pm3d
}
quit

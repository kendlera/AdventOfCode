
function scoreSquares(field, squareSize)
	xlim, ylim = size(field)
	bounds = squareSize-1
	scores = zeros(Int64, xlim-bounds, ylim-bounds)
	for x=1:xlim-bounds
		for y=1:ylim-bounds
			score = 0
			for xdist=0:bounds 
				for ydist=0:bounds
					score += field[x+xdist, y+ydist] 
				end
			end
			scores[x, y] = score 
		end
	end
	return findmax(scores)
end

function fillField(xlim, ylim)
	field = zeros(Int64, xlim, ylim)
	for x=1:xlim 
		for y=1:ylim
			step4 = ((((x + 10) * y) + 7672) * (x + 10))
			step5 = ((step4 % 1000) - (step4 % 100)) / 100
			field[x, y] = step5 - 5 
		end
	end
	for x=4:300
		println("Square Size ", x, ": ", scoreSquares(field, x))
	end
end

fillField(300, 300)
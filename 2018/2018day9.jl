

function playGame(numPlayers, numMarbles)
	stackOfMarbles = [0, 1]
	currentMarble = 2
	playerScore = Dict()
	for i = 2:numMarbles
		if (i%23) == 0
			# special case
			removedMarble = currentMarble - 7 
			if removedMarble < 1
				removedMarble = length(stackOfMarbles) + removedMarble 
			end
			currentPlayer = i%numPlayers
			if currentPlayer == 0
				# special case; probably some way to avoid?
				currentPlayer = numPlayers
			end
			playerScore[currentPlayer] = get(playerScore, currentPlayer, 0) + i + stackOfMarbles[removedMarble]
			splice!(stackOfMarbles, removedMarble)
			currentMarble = removedMarble
		else
			if currentMarble == length(stackOfMarbles)
				splice!(stackOfMarbles, 2:1, i)
				currentMarble = 2 
			else
				nextIndex = currentMarble + 2
				if nextIndex > length(stackOfMarbles)
					push!(stackOfMarbles, i)
				else
					splice!(stackOfMarbles, nextIndex:nextIndex-1, i)
				end
				currentMarble = nextIndex
			end
		end
		# println(stackOfMarbles)
	end
	return maximum(values(playerScore))
end

# println(playGame(470, 7217000))

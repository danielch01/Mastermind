# Build a Mastermind game from the command line where 
# you have 12 turns to guess the secret code, starting 
# with you guessing the computer's random code.

class Mastermind
	def initialize
		@turn = 0
		@maxturn = 12
		@game = false
		@choice = Array.new()
	end
	def play
		puts "----------------------------"
		puts "-- Welcome to Mastermind! --"
		puts "----------------------------\n\n"
		puts "Press enter to continue..."
		gets.chomp
		1.upto(4){@choice << (rand(5)+1).to_s}
		puts "The master code has been set. Please press enter to continue..."
		gets.chomp
		while(@game == false)
			if @turn == @maxturn
				puts "\n\nSorry, the code was: "
				@choice.each{|i| puts i}
				puts "Better luck next time!\n\n"
				break
			end
			user_choice = Array.new()
			puts "Choose numbers from 1 thru 6:"
			1.upto(4){user_choice << gets.chomp}
			r = 0
			w = 0
			4.times do |i|
				if user_choice.include? @choice[i]
					if user_choice[i] == @choice[i]
						r += 1
					else
						w += 1
					end
				end
			end
			puts "Red peg: " + r.to_s
			puts "White peg: " + w.to_s
			if r == 4
				puts "Congrats, you won!!!!\n\n"
				@game = true
			else
				if @turn < (@maxturn - 1)
					puts "\n\nSo close! Please try again\n\n"
				end
			end
			@turn += 1
		end
	end
end

Assingment 4. 01/10/18
======================================================

General notes:
======================================================

- This program constructs a maze for assignment 4, as well as loads one from file 
- There are 4 files in the archive: 
	maze.py - main file with generator
	node.py - file with class for room object
	input.txt - file where maze will be loaded from
	output.txt - file where created maze will be printed
- There are some additional files may appear in the process of compilation

- There are two ways of running the program: to construct the maze or load one from file

- A maze constructed using following parameters: N - total number of nodes, K - numer of border nodes, p - number of edges of normal nodes, k - number of edges of border nodes
	MM - number of monsters, WW - number of walls, GG - number of gold, HH - number of holes, as well as parameters for spread and decay

- N should be > K and p should be > k, otherwise error will be returned

- There is algorithm that checks if it possible to consruct the maze with entered K, N, k, p. If it is not possible, error will be returned
======================================================

Running the program
======================================================

 1. There is a folder inside an archive - assignment4. It should be extracted in any directory
 2. In terminal, change the directory to assignment4
 3. In the terminal, type: python maze.py
 4. Next, you will be asked if you want to create a maze or load one from a file

 	1. If you want to create one:

		1. type 'c' to the terminal

		2. Then enter parameters: N K p k 
			(in this order, separated by space) so that (N > K) and (p > k), otherwise error message will be printed

		3. Parameters will be checked wheter it is possible to construct the maze with them. If it not possible, "
			"maze cannot be constructed with this input" will be printed and you will be asked to enter them again

		4. If such maze could be construted, then enter parameters: MM HH GG WW 
			in this order and separated by space. Each of them should be less than N, otherwise error will be thrown.

		5. Then enter spread and decay, in this order and separated by space.

		6. The generated maze will be printed to the terminal and saved to the file output.txt

 	2. If you want to load one from file:

		1. type 'l' in the terminal
		
		2. Enter the representation of maze to be read into the file: input.txt

		3. Enter: input.txt spread decay
			Input should be exactly in this order and separated by space. Spread and decay are parameters

		4. It is assumed that maze will be loaded from file: input.txt. However, it can be loaded from any text file, which is in directory: assignment4
			In this case, type in terminal: filemane.txt spread decay 
			filename.txt should be in directory - assignment4

 		5. The format of the maze to be read from the file, should be as specified in the assignment: 6:1,1,0,0,1,0.5 7 2 3

			General format: 	id:W,H,M,G,w,s connected_rooms
			1. There should be no spaces if this part: id:W,H,M,G,w,s
			2. Connected_rooms should be separated by space
			Otherwise, input will not be read correctly			

			Example of correct input: 
			
			6:1,1,0,0,1,0.5 7 2 3
			7:0,1,0,1,1,0.25 6 1 5
			1:0,1,0,0,1,0.5 7 5 4
			3:0,0,1,0,0.5,1 6 4 2
			2:0,0,1,0,0.5,1 6 3
			5:0,0,0,0,0.5,0 7 1
			4:0,0,1,0,0.5,1 3 1

		6. The maze that was read will be printed to the terminal with updated values of smell and wind
=========================================================

Contact info:
=========================================================

Author: Abil' Kuatbayev
Email: abil.kuatbayev@nu.edu.kz

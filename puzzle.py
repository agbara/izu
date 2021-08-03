from random import choice
from time import time
from tkinter import*




def color_convert(r, g, b):
	return '#{:02x}{:02x}{:02x}'.format(int(r*2.55),int(g*2.55), int(b*2.55))

button_frame=Frame()
button_frame.configure(bg=color_convert(25,25,25))


root=Tk()


board1={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":" "}	
board={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":" "}
a_board={"1":["2","4"],"2":["1","3","5"],"3":["2","6"],"4":["1","5","7"],"5":["2","4","6","8"],"6":["3","5","9"],"7":["4","8"],"8":["5","7","9"],"9":["6","8"]}

brd={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":" "}

hour=00
minutes=00
seconds=00


watch=Label(button_frame,text="00:00:00",font=('verdana',5,'italic'),width=19,bg=color_convert(100,100,100))
watch.grid(row=0,column=2)


class Board_game:
	def __init__(self,board,board1,a_board,brd):
		self.board=board
		self.board1=board1
		self.a_board=a_board
		self.brd=brd
		
		
	def shuffle(self):
		empty_p=" "
		for i in self.board:
				if self.board[i]==" ":
					empty_p=i
		for i in range (200):
				b_choice=choice(self.a_board[empty_p])
				self.move(b_choice)
				empty_p=b_choice		
		global start
		start=time()
		self.update_timer()
		
	def update_timer(self):
		time_left = int(time()-start)
		global minutes
		minutes = time_left // 60
		global seconds
		seconds = time_left % 60
		global hour
		hour=minutes // 60
		watch.configure(text='{:02d}:{:02d}:{:02d}'.format(hour,minutes, seconds))
		root.after(100, self.update_timer)
	
	def stop_watch(self):
		if self.board==self.board1:
				watch.configure(text='{:02d}:{:02d}:{:02d}'.format(1,1,1))
				root.after(0, self.stop_watch)
				
	def reset_all(self):
		for i in self.board:
			self.board[i]=self.board1[i]	
		for i in self.brd:
			self.brd[i].configure(text=self.board[i])
	
	
	def move(self,a):
		g_move=False
		g_spot=100
		for i in self.a_board[a]:
			if self.board[i] ==" ":
				g_move=True
				g_spot=i
		if g_move:
			self.board[a],self.board[g_spot]=self.board[g_spot],self.board[a]
			self.brd[g_spot].configure(text=self.board[g_spot],bg=color_convert(0,25,0))
			self.brd[a].configure(text=self.board[a])
			
			
	def s_board(self):
		time=Label(button_frame,text="***Agbarakwe_izundu_auguatine .",font=('verdana',7,'italic'),width=27,bg=color_convert(25,25,25))
		time.grid(row=0,column=0,columnspan=2)
		
		root=Tk()
		self.brd["1"]=Button(button_frame,text=self.board["1"],font=('Verdana',63),width=1,bg=color_convert(0,25,0),command=lambda a="1": self.move(a))
		self.brd["1"].grid(row=1,column=0)
		
		self.brd["2"]=Button(button_frame,text=self.board["2"],font=('Verdana',63),width=1,bg=color_convert(0,25,0),command=lambda a="2": self.move(a))
		self.brd["2"].grid(row=1,column=1)
		
		self.brd["3"]=Button(button_frame,text=self.board["3"],font=('Verdana',63),width=1,bg=color_convert(0,25,0),command=lambda a="3": self.move(a))
		self.brd["3"].grid(row=1,column=2)
		
		self.brd["4"]=Button(button_frame,text=self.board["4"],font=('Verdana',63),width=1,bg=color_convert(0,25,0),command=lambda a="4": self.move(a))
		self.brd["4"].grid(row=2,column=0)
		
		self.brd["5"]=Button(button_frame,text=self.board["5"],font=('Verdana',63),width=1,bg=color_convert(0,25,0),command=lambda a="5": self.move(a))
		self.brd["5"].grid(row=2,column=1)
		
		self.brd["6"]=Button(button_frame,text=self.board["6"],font=('Verdana',63),width=1,bg=color_convert(0,25,0),command=lambda a="6": self.move(a))
		self.brd["6"].grid(row=2,column=2)
		
		self.brd["7"]=Button(button_frame,text=self.board["7"],font=('Verdana',63),width=1,bg=color_convert(0,25,0),command=lambda a="7": self.move(a))
		self.brd["7"].grid(row=3,column=0)
		
		self.brd["8"]=Button(button_frame,text=self.board["8"],font=('Verdana',63),width=1,bg=color_convert(0,25,0),command=lambda a="8": self.move(a))
		self.brd["8"].grid(row=3,column=1)
		
		self.brd["9"]=Button(button_frame,text=self.board["9"],font=('Verdana',63),width=1,command=lambda a="9": self.move(a))
		self.brd["9"].grid(row=3,column=2)
		
		time1=Label(button_frame,text="\n"*3,bg=color_convert(25,25,25))
		time1.grid(row=4,column=0,columnspan=3)
		
		
		reset=Button(button_frame,text="reset",font=('verdana',12,'italic'),width=5,bg=color_convert(55,35,55),command=self.reset_all)
		reset.grid(row=4,column=0)
		
		shuffle=Button(button_frame,text="shuffle",font=('verdana',12,'italic'),width=5,bg=color_convert(55,55,35),command=self.shuffle)
		shuffle.grid(row=4,column=1)
		
		stop=Button(button_frame,text="stop",font=('verdana',12,'italic'),width=5,bg=color_convert(35,55,35),command=self.stop_watch)
		stop.grid(row=4,column=2)
				
		
button_frame.grid(row=0, column=0)

play=Board_game(board,board1,a_board,brd)

play.s_board()



mainloop()
import customtkinter as ctk
import sudoku


class MyGUI:
        
        def __init__(self):
                ctk.set_appearance_mode("dark")
                self.display = ctk.CTk()
                self.display.geometry('600x600')
                self.display.protocol("WM_DELETE_WINDOW", self.on_close)
                self.openingPage()
                self.display.mainloop()

      
        def on_close(self):
            self.display.destroy()

        def openingPage(self):
                self.clearFrame(self.display)

                self.welcomeFrame = ctk.CTkFrame(self.display)
                self.welcomeFrame.grid()

                title = ctk.CTkLabel(self.welcomeFrame, text = "Welcome to Sudoku!", font = ("Ariel", 35))
                title.grid(row = 0, column = 0, padx = 140, pady = 50)

                rules_text = "Objective: \n Fill cells with numbers 1-9 until the board is complete.\n \n Rules: \n 1) Each 3x3 box, row, and column must contain numbers 1-9 \n 2) Numbers in 3x3 boxes, rows, and columns cannot repeat"
                rules = ctk.CTkLabel(self.welcomeFrame, text = rules_text, font = ("Ariel", 15))
                rules.grid(pady = 25)

                start_button = ctk.CTkButton(self.welcomeFrame, text = "Start Game", command = self.createBoard)
                start_button.grid(pady = (50, 250))
      
        def endingPage(self):
              self.clearFrame(self.display)

              self.endingFrame = ctk.CTkFrame(self.display)
              self.endingFrame.grid()

              message = ctk.CTkLabel(self.endingFrame, text = "Congratulations! You've completed the puzzle!", font = ("Ariel", 18))
              message.grid(padx = 140, pady = (50, 550))
               
        def clearFrame(self, frame):
                for widget in frame.winfo_children():
                        widget.destroy()

        def createBoard(self):

                self.clearFrame(self.display)
        
                heading = ctk.CTkLabel(self.display, text = "Sudoku", font = ("Ariel", 25))
                heading.grid(row = 0, column = 0, padx = 250, pady = (25, 50))

                self.grid_frame = ctk.CTkFrame(self.display, fg_color = "blue")
                self.grid_frame.grid(row = 1, column = 0)

                self.all_entries = []

                self.autocheck_var = ctk.IntVar(value = 0)
                self.autocheck = ctk.CTkCheckBox(self.display, text = "Autocheck", variable = self.autocheck_var, command = self.autocheckToggle)
                self.autocheck.grid(pady = (35, 0))

                hiddenSquares = 0
                
                for row in range(9):
                      displayed = 0
                      row_entries = []
                      for col in range(9):
                        
                        element = nums.playingBoard[row][col]
                        entry = ctk.CTkEntry(self.grid_frame, width = 45, height = 45)
                        if row == 0 or row == 3 or row == 6:
                              entry.grid(row = row, column = col, pady = (3, 0))
                        elif row == 8:
                              entry.grid(row = row, column = col, pady = (0, 3))
                        elif col == 0 or col == 3 or col == 6:
                              entry.grid(row = row, column = col, padx = (3, 0))
                        elif col == 8:
                              entry.grid(row = row, column = col, padx = (0, 3))
                        else:
                              entry.grid(row = row, column = col) 
                        random_number = sudoku.random.randint(1, 5)
                        if random_number >= 3 and hiddenSquares < 40 and displayed < 6:
                              entry.insert(25, element)
                              hiddenSquares += 1
                              displayed += 1
                        row_entries.append(entry)
                  
      

                        def bind_autocheck(event, row=row, col=col):
                              if self.autocheck_var.get() == 1:
                                    self.checkInput(event, row, col)
                              else:
                                    self.all_entries[row][col].configure(text_color = "white")
                              if self.checkBoard():
                                    self.endingPage()

                        entry.bind("<KeyRelease>", bind_autocheck)

                      self.all_entries.append(row_entries)

        def autocheckToggle(self):
              if self.autocheck_var.get() == 1:
                    self.updateColor()


        def checkInput(self, event, row, col):
                text = self.all_entries[row][col].get()
                if text == str(nums.playingBoard[row][col]):
                      self.all_entries[row][col].configure(text_color = "white")
                else:
                      self.all_entries[row][col].configure(text_color = "red")

        def updateColor(self):
               for i in range(9):
                    for j in range(9):
                        element = self.all_entries[i][j].get()
                        if len(element) > 0 and element != str(nums.playingBoard[i][j]):
                              self.all_entries[i][j].configure(text_color = "red")

        def checkBoard(self):
              complete = True
              exit_loops = False

              for i in range(9):
                    for j in range(9):
                          if self.all_entries[i][j].get() != str(nums.playingBoard[i][j]):
                                complete = False
                                exit_loops = True
                                break
                          if exit_loops:
                                break
                          
              return complete
nums = sudoku.board()
board = MyGUI()
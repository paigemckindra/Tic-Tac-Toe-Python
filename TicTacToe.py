class TickTackToe() :
  def __init__(self, x, o) :
    self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self.move = 1
    self.p1 = x
    self.p2 = o

  # def makeBoard(self) :
  #   self.board =

  def printBoard(self, ) :
    for y in range(3) :
      for x in range(3) :
        print self.board[y][x],
      print


  def updateBoard(self, x, y, player) :
    if player == 'x' :
      self.board[y][x] = 'x'
    else :
      self.board[y][x] = 'o'


  def checkWin(self, player) :
    for i in self.board:
      if i.count(player) == 3 :
        return True

    for y in range(3) :
      count = 0
      for x in range(3) :
        if self.board[x][y] == player :
          count += 1
      if count == 3 :
        return True

    count = 0
    for i in range(3) :
      if self.board[i][i] == player :
        count += 1
    if count == 3 :
      return True
    else :
      return False

  def startGame(self,) :
    # self.makeBoard()
    self.printBoard()
    game_over = False
    while not game_over :
      if self.move % 2 != 0 :
        print "Enter the coordinates of your move x: "
        raw = raw_input()
        if self.board[int(raw[0])][int(raw[1])] != 0:
          print "Invalid move you lose your turn!"
          self.move += 1
          continue
        self.updateBoard(int(raw[0]), int(raw[1]), self.p1)
        self.printBoard()
        game_over = self.checkWin(self.p1)
        if (game_over) :
          print 'x Won'
      else :
        print "Enter the coordinates of your move o: "
        raw = raw_input()
        if self.board[int(raw[0])][int(raw[1])] != 0 :
          print "Invalid move you lose your turn!"
          self.move += 1
          continue
        self.updateBoard(int(raw[0]), int(raw[1]), self.p2)
        self.printBoard()
        game_over = self.checkWin(self.p2)
        if (game_over) :
          print 'o Won'
      self.move += 1

game = TickTackToe('x', 'o')
game.startGame()

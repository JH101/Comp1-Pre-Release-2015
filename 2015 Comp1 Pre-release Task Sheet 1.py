# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

def FindOpposingSarrum(Board, WhoseTurn):
  try:
    if WhoseTurn == "W":
      SarrumPosition = None
      Rank = 1
      File = 1
      while SarrumPosition == None:
        for count in range(1, BOARDDIMENSION):
          for count in range(1, BOARDDIMENSION):
              PieceType = Board[Rank][File]
              if PieceType == "BS":
                SarrumPosition = Board[Rank][File]
              else:
                File = File + 1
        Rank = Rank + 1
      print("Opposing Sarrum is at F{0}R{1}".format(File, Rank-1))
    else:
      SarrumPosition = None
      Rank = 1
      File = 1
      while SarrumPosition == None:
        for count in range(1, BOARDDIMENSION):
          for count in range(1, BOARDDIMENSION):
              PieceType = Board[Rank][File]
              if PieceType == "WS":
                SarrumPosition = Board[Rank][File]
              else:
                File = File + 1
        Rank = Rank + 1
      print("Opposing Sarrum is at F{0}R{1}".format(File, Rank-1))
  except IndexError:
    if WhoseTurn != "W":
      SarrumPosition = None
      Rank = 1
      while SarrumPosition == None:
        for count in range(1, BOARDDIMENSION):
          file = 1
          for count in range(1, BOARDDIMENSION):
              PieceType = Board[Rank][File]
              if PieceType == "WS":
                SarrumPosition = Board[Rank][File]
              else:
                Rank = Rank + 1
        File = File + 1
      print("Opposing Sarrum is at F{0}R{1}".format(File-1, Rank))
    else:
      SarrumPosition = None
      Rank = 1
      File = 1
      while SarrumPosition == None:
        for count in range(1, BOARDDIMENSION):
          for count in range(1, BOARDDIMENSION):
              PieceType = Board[Rank][File]
              if PieceType == "WS":
                SarrumPosition = Board[Rank][File]
              else:
                Rank = Rank + 1
        File = File + 1
      print("Opposing Sarrum is at F{0}R{1}".format(File-1, Rank))

def GetPieceName(Board, StartRank, StartFile, FinishRank, FinishFile):
  Team1PieceType = Board[StartRank][StartFile][1]
  Team1PieceColour = Board[StartRank][StartFile][0]
  if Team1PieceColour == "W":
    PieceColour1 = "White"
  else:
    PieceColour1 = "Black"
  if Team1PieceType == "R":
    PieceType1 = "Redum"        
  elif Team1PieceType == "S":
    PieceType1 = "Sarrum"
  elif Team1PieceType == "M":
    PieceType1 = "Marzaz Pani"
  elif Team1PieceType == "G":
    PieceType1 = "Gisgigir"
  elif Team1PieceType == "N":
    PieceType1 = "Nabu"
  elif Team1PieceType == "E":
    PieceType1 = "Eltu"
  Team2PieceType = Board[FinishRank][FinishFile][1]
  Team2PieceColour = Board[FinishRank][FinishFile][0]
  if Team2PieceColour == "W":
    PieceColour2 = "White"
  elif Team2PieceColour == "B":
    PieceColour2 = "Black"
  else:
    PieceColour2 = ("F{0}".format(FinishFile))
  if Team2PieceType == "R":
    PieceType2 = "Redum"        
  elif Team2PieceType == "S":
    PieceType2 = "Sarrum"
  elif Team2PieceType == "M":
    PieceType2 = "Marzaz Pani"
  elif Team2PieceType == "G":
    PieceType2 = "Gisgigir"
  elif Team2PieceType == "N":
    PieceType2 = "Nabu"
  elif Team2PieceType == "E":
    PieceType2 = "Eltu"  
  else:
    PieceType2 = ("R{0}".format(FinishRank))
  return PieceColour1, PieceType1, PieceColour2, PieceType2

def ConfirmMove(StartSquare, FinishSquare):
  StartStr = str(StartSquare)
  FinishStr = str(FinishSquare)
  print()
  print("Move from Rank {0}, File {1} to Rank {2}, File {3}?".format(StartStr[0], StartStr[1], FinishStr[0], FinishStr[1]))
  Confirm = input("Confirm move (Yes/No): ")
  return Confirm.lower()[0]

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  valid = False
  while valid == False:
    TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
    if TypeOfGame.lower()[0] == "n" or TypeOfGame.lower()[0] == "y":
      valid = True
    else:
      print("Please enter a correct value")
  return TypeOfGame.lower()[0] 

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     -------------------------")
    print("R{0}".format(RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("     F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  try:
    MoveIsLegal = True
    if (FinishFile == StartFile) and (FinishRank == StartRank):
      MoveIsLegal = False
    else:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
      if WhoseTurn == "W":
        if PieceColour != "W":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "W":
          MoveIsLegal = False
      else:
        if PieceColour != "B":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
      if MoveIsLegal == True:
        if PieceType == "R":
          MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
        elif PieceType == "S":
          MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "M":
          MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "G":
          MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "N":
          MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "E":
          MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
    return MoveIsLegal
  except IndexError:
    MoveIsLegal = False
    return MoveIsLegal
    
def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG"
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
  else:
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "    
                    
def GetMove(StartSquare, FinishSquare):
  valid = False
  while valid == False:
    try:
      StartSquarevalid = False
      while StartSquarevalid == False:
        StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
        if StartSquare%10 == 0 or StartSquare%10 == 9 or StartSquare/10 < 1:
          print("Please provide a Valid File AND Rank for this move")
        else:
          StartSquarevalid = True  
      FinishSquarevalid = False
      while FinishSquarevalid == False:
        FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
        if FinishSquare%10 == 0 or FinishSquare%10 == 9 or FinishSquare/10 < 1:
          print("Please provide a Valid File AND Rank for this move")
        else:
          FinishSquarevalid = True
      valid = True
      return StartSquare, FinishSquare
    except ValueError:
      print("Please provide a Valid File AND Rank for this move")
      valid = False

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn, PieceColour1, PieceType1, PieceColour2, PieceType2):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    print()
    print("{0} {1} takes {2} {3}".format(PieceColour1, PieceType1, PieceColour2, PieceType2))
    print("White Redum Promoted to Mazaz Pani")
    Board[StartRank][StartFile] = "  "
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    print()
    print("{0} {1} takes {2} {3}".format(PieceColour1, PieceType1, PieceColour2, PieceType2))
    print("Black Redum, Promoted to Marzaz Pani.")
    Board[StartRank][StartFile] = "  "
  else:
    print()
    print("{0} {1} takes {2} {3}".format(PieceColour1, PieceType1, PieceColour2, PieceType2))
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
    
    
if __name__ == "__main__":
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    SampleGame = GetTypeOfGame()
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      Confirm = "n"
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      while Confirm == "n":
        Rank = 1
        File = 1
        FindOpposingSarrum(Board, WhoseTurn)
        MoveIsLegal = False
        while not(MoveIsLegal):
          StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
          StartRank = StartSquare % 10
          StartFile = StartSquare // 10
          FinishRank = FinishSquare % 10
          FinishFile = FinishSquare // 10
          MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if not(MoveIsLegal):
            print("That is not a legal move - please try again")
        GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
        Confirm = ConfirmMove(StartSquare, FinishSquare)
        if Confirm == "y":
          print("Move Confirmed")
          PieceColour1, PieceType1, PieceColour2, PieceType2 = GetPieceName(Board, StartRank, StartFile, FinishRank, FinishFile)
          MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn, PieceColour1, PieceType1, PieceColour2, PieceType2)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)

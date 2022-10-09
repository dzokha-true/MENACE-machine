import numpy
import random
import pickle
import os.path


def allEqualTo(values, test):
    for key, value in values.items():
        if value != test:
            return False
    return True


def weightedPick(dic):
    total = sum(dic.itervalues())
    pick = random.randint(0, total - 1)
    tmp = 0
    for key, weight in dic.iteritems():
        tmp += weight
        if pick < tmp:
            return key


class tic_tac_toe:

    def resetBoard(self):
        self.game = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        # Use player2 and player3 to keep internal logic consustent, (using 2 nad

    # 3 to mark positions on the board)
    def setPlayers(self, player2, player3):
        self.players = {2: player2, 3: player3}

    def swapPlayers(self):
        self.setPlayers(self.players[3], self.players[2])

    def playGame(self, first=2):
        self.resetBoard()
        self.tellPlayersAboutNewGame()

        gameState = self.gameState()
        player = first

        while gameState['inPlay']:
            self.makePlayerMove(player)
            player = 2 if player == 3 else 3
            gameState = self.gameState()

        self.tellPlayersResult(gameState)

    def makePlayerMove(self, playerNum):
        # convert grid so that player is ignorant on wheter they are 2 or 3
        # U for 'you' the active player, O for 'opponent'
        oponentNum = 2 if playerNum == 3 else 3
        convertedGrid = str(self.game)
        convertedGrid = convertedGrid.replace(str(playerNum), 'U') \
            .replace(str(oponentNum), 'O')
        player = self.players[playerNum]
        move = player.makeMove(convertedGrid, self.possibleMoves())
        self.updateBoard(move, playerNum)

    def updateBoard(self, move, playerNum):
        self.game[int(move / 3), (move) % 3] = playerNum

    def tellPlayersAboutNewGame(self):
        for key, player in self.players.items():
            player.startNewGame()

    def tellPlayersResult(self, result):
        if result['draw']:
            for key, player in self.players.items():
                player.setResult('draw')
        else:
            for key, player in self.players.items():
                player.setResult('win' if key == result['winner'] else 'lose')

    def gameState(self):
        for le in [2, 3]:
            v = le ** 3
            if (v in numpy.prod(self.game, 0)) or (le ** 3 in \
                                                   numpy.prod(self.game, 1)) or (v == \
                                                                                 numpy.prod(
                                                                                     numpy.diagonal(self.game))) or \
                    (v == numpy.prod(numpy.diagonal(numpy.flipud(self.game)))):
                return {'inPlay': False, 'draw': False, 'winner': le}

        if (numpy.prod(self.game) == 0):
            return {'inPlay': True}
        return {'inPlay': False, 'draw': True}

    def possibleMoves(self):
        a = numpy.where(self.game == 0)
        return (a[0] * 3) + a[1]


class comp_player:
    def __init__(self, training, strategyFile=""):
        self.gameHistory = {}
        self.noLoseStreak = 0
        self.training = training

        if strategyFile != "":
            if os.path.exists(strategyFile):
                with open(strategyFile, "rb") as inp:
                    self.strategy = pickle.load(inp)
                    return None
            else:
                print
                'Strategy file not found, using blank tempelate'
        self.strategy = {}

    def saveStrategy(self, strategyFile):
        with open(strategyFile, "wb") as output:
            pickle.dump(self.strategy, output, pickle.HIGHEST_PROTOCOL)

    def makeMove(self, gameState, possibleMoves):
        # check if the state isnt in strategy or its all 0s, sets to balanced,
        # original MENACE would have a give up feature for all 0s but it
        # might be bad luck
        if (gameState not in self.strategy or \
                allEqualTo(self.strategy[gameState], 0)):
            self.strategy[gameState] = dict.fromkeys(possibleMoves, 5)

        move = weightedPick(self.strategy[gameState])
        self.gameHistory[gameState] = move
        return move

    def setResult(self, result):
        if self.training:
            transl = {"win": 3, "lose": -1, "draw": 0}
            countChange = transl[result]
            for state in self.gameHistory:
                move = self.gameHistory[state]
                self.strategy[state][move] += countChange

                if result == "lose":
                    self.noLoseStreak = 0
                else:
                    self.noLoseStreak += 1

    def setTraining(self, value):
        self.training = value

    def startNewGame(self):
        self.gameHistory = {}

    # for each state make the most likely move the only move
    def optStrategy(self):
        for state in self.strategy:
            strategy = self.strategy[state]
            counterMax = 0

            for move in strategy:
                if strategy[move] > counterMax:
                    counterMax = strategy[move]
                    bestMove = move

            # must go in reverse
            keys = strategy.keys()
            keys.reverse()

            for move in keys:
                if move != bestMove:
                    del strategy[move]


# valifate each input
# nicer words
class human_player():
    def __init__(self, d=False):

        if d:
            self.name = 'Human'
            self.identity = 'X'
            self.opponent = "O"
        else:
            self.name = str(raw_input("What's Your name? \n"))
            self.identity = str(raw_input('Would you like to be X or O? \n'))
            self.identity.upper()
            self.opponent = "O" if self.identity == "X" else "X"

    def startNewGame(self):
        print
        self.name + '! New Game Starting!'

    def makeMove(self, gameState, possibleMoves):
        print
        gameState.replace("O", self.opponent).replace("U", self.identity)
        # maybe make game return normal Board for a human player - but then
        # would have to calculate wins and losses seperately
        print
        str(self.name) + ' ,your moves are ' + str(possibleMoves)
        move = int(input("Enter your move "))
        return move

    def setResult(self, result):
        print
        result


class random_player():
    def startNewGame(self):
        return;

    def makeMove(self, gameState, possibleMoves):
        return numpy.random.choice(possibleMoves)

    def setResult(self, result):
        return;


# ==============================================================================

# only trains the player in being first
def getTrained(numTrials, playerToTrain=None):
    if (playerToTrain == None):
        playerToTrain = comp_player(True)
    a = comp_player(True)
    b = random_player()
    game1 = tic_tac_toe()
    game2 = tic_tac_toe()
    game3 = tic_tac_toe()
    game1.setPlayers(playerToTrain, a)
    game2.setPlayers(playerToTrain, b)
    game3.setPlayers(a, b)

    for i in range(numTrials):
        game1.playGame()
        game2.playGame()
        game3.playGame()

    return playerToTrain
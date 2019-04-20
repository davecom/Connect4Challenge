# connectfour.py
# The C4Board and C4Piece classes that form the heart of a
# game of Connect Four
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations
from typing import List, Optional, Tuple
from enum import Enum
from board import Piece, Board, Move

# Do Not Modify
class C4Piece(Piece, Enum):
    B = "B"
    R = "R"
    E = " " # stand-in for empty

    @property
    def opposite(self) -> C4Piece:
        if self == C4Piece.B:
            return C4Piece.R
        elif self == C4Piece.R:
            return C4Piece.B
        else:
            return C4Piece.E

    def __str__(self) -> str:
        return self.value


# The main class that should extend the Board abstract base class
# It maintains the position of a game
# You should not need to add any additional properties to this class, but
# you may add additional methods
class C4Board(Board):
    # Class variables
    # Do Not Modify the existing ones, but
    # feel free to add more
    NUM_ROWS: int = 6
    NUM_COLUMNS: int = 7
    SEGMENT_LENGTH: int = 4

    # This inner helper class is usesd by C4Board
    # It represents a single column of pieces
    # Do Not Modify this class
    class Column:
        def __init__(self) -> None:
            self._container: List[C4Piece] = []

        @property
        def full(self) -> bool:
            return len(self._container) == C4Board.NUM_ROWS

        def push(self, item: C4Piece) -> None:
            if self.full:
                raise OverflowError("Trying to push piece to full column")
            self._container.append(item)

        def __getitem__(self, index: int) -> C4Piece:
            if index > len(self._container) - 1:
                return C4Piece.E
            return self._container[index]

        def __repr__(self) -> str:
            return repr(self._container)

        def copy(self) -> C4Board.Column:
            temp: C4Board.Column = C4Board.Column()
            temp._container = self._container.copy()
            return temp

    # You should not need to modify
    # this constructor
    def __init__(self, position: Optional[List[C4Board.Column]] = None, turn: C4Piece = C4Piece.B) -> None:
        if position is None:
            self.position: List[C4Board.Column] = [C4Board.Column() for _ in range(C4Board.NUM_COLUMNS)]
        else:
            self.position = position
        self._turn: C4Piece = turn

    # Who's turn is it?
    @property
    def turn(self) -> Piece:
        # Your Code Here

    # Put a piece in column location.
    # Returns a *copy* of the board with the move made.
    # Does not check if the column is full (assumes legal move).
    def move(self, location: Move) -> Board:
        # Your Code Here

    # All of the current legal moves.
    # Remember, a move is just the column you can play.
    @property
    def legal_moves(self) -> List[Move]:
        # Your Code Here

    # Is it a win?
    @property
    def is_win(self) -> bool:
        # Your Code Here

    # Who is winning in this position?
    # This function scores the position for player
    # and returns a numerical score
    # When player is doing well, the score should be higher
    # When player is doing worse, player's returned score should be lower
    # Scores mean nothing except in relation to one another; so you can
    # use any scale that makes sense to you
    # The more accurately evaluate() scores a position, the better that minimax will work
    # There may be more than one way to evaluate a position but an obvious route
    # is to count how many 1 filled, 2 filled, and 3 filled segments of the board
    # that the player has (that don't include any of the opponents pieces) and give
    # a higher score for 3 filleds than 2 filleds, 1 filleds, etc.
    # You may also need to score wins (4 filleds) as very high scores and losses (4 filleds
    # for the opponent) as very low scores
    def evaluate(self, player: Piece) -> float:
        # Your Code Here

    # Print the board nicely
    def __repr__(self) -> str:
        # Your Code Here


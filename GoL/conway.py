# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal
import rle
import time 

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.int64)
        self.neighborhood = np.ones((3,3), np.int64) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.N = N
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()
               
    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        start_time = time.time()
        #get weighted sum of neighbors
        #PART A & E CODE HERE

        if self.fastMode:
            neighbor_count = signal.convolve2d(self.grid, self.neighborhood, mode='same', boundary='wrap', fillvalue=0)
            new_grid = np.where((self.grid == self.aliveValue) & ((neighbor_count < 2) | (neighbor_count > 3)), 
                                self.deadValue, self.grid)
            new_grid = np.where((self.grid == self.deadValue) & (neighbor_count == 3), self.aliveValue, new_grid)
            self.grid = new_grid
        else:
        #implement the GoL rules by thresholding the weights
        #PART A CODE HERE
            new_grid = np.zeros((self.N, self.N), np.int64)
            for i in range(self.N):
                for j in range(self.N):
                    neighbor_count = self.count_neighbors((i,j))
                    if self.grid[i][j] == self.aliveValue:
                        if neighbor_count < 2 or neighbor_count > 3:
                             new_grid[i][j] = self.deadValue
                        else:
                            new_grid[i][j] = self.aliveValue
                    else:
                        if neighbor_count == 3:
                            new_grid[i][j] = self.aliveValue
            self.grid = new_grid
        
    
    def count_neighbors(self, cell):
        # Count the number of alive cells (neighbors) around a given cell
        i, j = cell
        count = 0
        for x in range(max(0, i-1), min(self.N, i+2)):
            for y in range(max(0, j-1), min(self.N, j+2)):
                if (x, y) != (i, j) and self.grid[x][y] == self.aliveValue:
                    count += 1
        return count   

    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        # error in it 
        self.grid[index[0]+1, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+23] = self.aliveValue
        self.grid[index[0]+2, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+13] = self.aliveValue
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+35] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+12] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+35] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+11] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+21] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+11] = self.aliveValue
        self.grid[index[0]+6, index[1]+15] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        self.grid[index[0]+6, index[1]+23] = self.aliveValue
        self.grid[index[0]+6, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+17] = self.aliveValue
        self.grid[index[0]+7, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+16] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+13] = self.aliveValue
        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        
    def insertFromPlainText_direct(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human readable pattern without comments
        '''
        max_x_offset = 0
        max_y_offset = 0
        with open(txtString, 'r') as file:
            for line in file:
                if not line.startswith("!"):
                    line = line.strip()
                    max_x_offset = max(max_x_offset, len(line))
                    max_y_offset += 1
    
        new_N = max(self.N, max_x_offset + 48)
        new_grid = np.zeros((new_N, new_N), np.int64)

        with open(txtString, 'r') as file:
            y = 0
            for line in file:
                if not line.startswith("!"):
                    line = line.strip()
                    for x, char in enumerate(line):
                        if char == "O":
                            new_grid[y+24][x+24] = self.aliveValue
                        else:
                            new_grid[y+24][x+24] = self.deadValue
                    y += 1

        self.grid = new_grid
        self.N = new_N

    def insertFromPlainText(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human readable pattern without comments
        '''
        lines = txtString.split("\n")
        
        max_x_offset = 0
        max_y_offset = 0

        for line in lines:
            if not line.startswith("!"):
                line_length = len(line.strip())
                if line_length > max_x_offset:
                    max_x_offset = line_length
                max_y_offset += 1

        new_N = max(self.N, max_x_offset + 48)
        new_grid = np.zeros((new_N, new_N), np.int64)

        y = 0
        for line in lines:
            if not line.startswith("!"):
                line = line.strip()
                for x, char in enumerate(line):
                    if char == "O":
                        new_grid[y+pad][x+pad] = self.aliveValue
                    else:
                        new_grid[y+pad][x+pad] = self.deadValue
                y += 1

        self.grid = new_grid
        self.N = new_N

    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''

        parser = rle.RunLengthEncodedParser(rleString)
        pattern = parser.pattern_2d_array
        pattern_height, pattern_width = len(pattern), len(pattern[0])

        new_N = max(pattern_height + pad, pattern_width + pad)

        new_grid = np.zeros((new_N, new_N), np.int64)

        start_x = (new_N - pattern_width) // 2
        start_y = (new_N - pattern_height) // 2

        for x in range(pattern_height):
            for y in range(pattern_width):
                if pattern[x][y] != 'b': 
                    new_grid[start_y + x][start_x + y] = self.aliveValue
                else:
                    new_grid[start_y + x][start_x + y] = self.deadValue

        self.grid = new_grid
        self.N = new_N



        
#!/usr/bin/python3

"""Rotating a two-dimensional matrix 90degress clockwise"""

def rotate_2d_matrix(matrix):
  rotateLeft = 0,
  rotateRight = 0,
  len(matrix) - 1
  
  while rotateLeft < rotateRight:
    for i in range(rotateRight -rotateLeft):
      top = rotateLeft,
      bottom = rotateRight
      topRotateLeft = matrix[top][rotateLeft + i]
      
      matrix[top][rotateLeft + i] = matrix[bottom -i][rotateLeft]
      matrix[bottom - i][rotateLeft]= matrix[bottom][rotateRight - i]
      matrix[bottom][rotateRight - i] = matrix[top + i][rotateRight]
      matrix[top + i][rotateRight] = topRotateLeft
    
    rotateLeft = rotateLeft + 1
    rotateRight = rotateRight - 1
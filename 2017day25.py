

def operator():
  steps = 12399302
  tape = [0] * (steps)
  cursor = steps // 2 
  state = 'A'
  for step in range(steps):
    if state == 'A':
      if tape[cursor] == 0:
        tape[cursor] = 1
        state = 'B'
      else:
        tape[cursor] = 0
        state = 'C'
      cursor += 1
    elif state == 'B':
      if tape[cursor] == 0:
        cursor -= 1 
        state = 'A'
      else:
        tape[cursor] = 0 
        cursor += 1
        state = 'D'
    elif state == 'C':
      if tape[cursor] == 0:
        tape[cursor] = 1 
        state = 'D'
      else:
        state = 'A'
      cursor += 1 
    elif state == 'D':
      if tape[cursor] == 0:
        tape[cursor] = 1 
        state = 'E'
      else:
        tape[cursor] = 0 
      cursor -= 1
    elif state == 'E':
      if tape[cursor] == 0:
        tape[cursor] = 1 
        cursor += 1 
        state = 'F'
      else:
        cursor -= 1 
        state = 'B'
    elif state == 'F':
      if tape[cursor] == 0:
        tape[cursor] = 1 
        state = 'A'
      else:
        state = 'E'
      cursor += 1 
  print(sum(tape))

# operator()

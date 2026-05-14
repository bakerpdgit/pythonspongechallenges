# Turtle Memory Challenge

In this challenge, the computer turtle draws a random path using only 90° turns and forward distances.
You watch, then the drawing is cleared.
Your job is to redraw the path from memory.

## How to run

1. Open a terminal in this folder.
2. Run:

```bash
python turtle_memory_challenge.py
```

3. Controls while playing:
   - `Up Arrow`: move forward 10 pixels
   - `Left Arrow`: turn left 90°
   - `Right Arrow`: turn right 90°
   - `x`: finish your attempt and get a score
   - `Space`: start a new round

## Your tasks

- **TASK 1:** Change `NUMBER_OF_MOVES` to make the memory path shorter or longer.
- **TASK 2:** Change `SHOW_TIME_MS` so the player gets more or less time to watch.
- **TASK 3:** Stop the computer path from going too close to the edge of the window.
- **TASK 4:** Improve scoring so it checks more than just exact move order.
- **TASK 5:** Add a second round and keep a total score across rounds.

## Extensions

1. Add difficulty levels (easy/medium/hard) with different path lengths.
2. Show the original path at the end in a different color so players can compare.
3. Add lives: each round costs one life if the score is below a target.

import 'dart:convert';
import 'dart:io';
import 'dart:collection';

(int, int)? findStart(List<String> maze) {
  for (int y = 0; y < maze.length; y++) {
    var x = maze[y].indexOf('S');
    if (x != -1) {
      return (y, x);
    }
  }
  return null;
}

int calculateInsideTileCount(List<String> maze, (int, int) start) {
  final height = maze.length;
  final width = maze[0].length;
  var queue = Queue<(int, int)>.from([start]);
  var moves = Set<(int, int)>.from([start]);
  var actualS = Set<String>.from(['|', '-', 'J', 'L', '7', 'F']);
  while (queue.isNotEmpty) {
    final (y, x) = queue.removeFirst();
    final c = maze[y][x];
    if ((y > 0) &&
        'S|JL'.contains(c) &&
        '|7F'.contains(maze[y - 1][x]) &&
        !moves.contains((y - 1, x))) {
      moves.add((y - 1, x));
      queue.addLast((y - 1, x));
      if (c == 'S') {
        actualS = actualS.intersection(Set.from(['|', 'J', 'L']));
      }
    }
    if ((y < height) &&
        'S|7F'.contains(c) &&
        '|JL'.contains(maze[y + 1][x]) &&
        !moves.contains((y + 1, x))) {
      moves.add((y + 1, x));
      queue.addLast((y + 1, x));
      if (c == 'S') {
        actualS = actualS.intersection(Set.from(['|', '7', 'F']));
      }
    }
    if ((x > 0) &&
        'S-J7'.contains(c) &&
        '-LF'.contains(maze[y][x - 1]) &&
        !moves.contains((y, x - 1))) {
      moves.add((y, x - 1));
      queue.addLast((y, x - 1));
      if (c == 'S') {
        actualS = actualS.intersection(Set.from(['-', 'J', '7']));
      }
    }
    if ((x < width) &&
        'S-LF'.contains(c) &&
        '-J7'.contains((maze[y][x + 1])) &&
        !moves.contains((y, x + 1))) {
      moves.add((y, x + 1));
      queue.addLast((y, x + 1));
      if (c == 'S') {
        actualS = actualS.intersection(Set.from(['-', 'L', 'F']));
      }
    }
  }
  final s = actualS.first;
  maze = [for (String line in maze) line.replaceFirst('S', s)];
  for (int y = 0; y < height; y++) {
    var line = maze[y];
    var buffer = StringBuffer();
    for (int x = 0; x < width; x++) {
      var c = line[x];
      if (!moves.contains((y, x))) {
        c = '.';
      }
      buffer.write(c);
    }
    maze[y] = buffer.toString();
  }
  var outsideTiles = Set<(int, int)>();
  for (int y = 0; y < height; y++) {
    final line = maze[y];
    var outside = true;
    var vertical = false;
    for (int x = 0; x < width; x++) {
      final c = line[x];
      switch (c) {
        case '|':
          outside = !outside;
        case '-':
          break;
        case 'L' || 'F':
          vertical = (c == 'L');
        case '7' || 'J':
          if (c != (vertical ? 'J' : '7')) {
            outside = !outside;
          }
          vertical = false;
        case '.':
          break;
        default:
          break;
      }
      if (outside) {
        outsideTiles.add((y, x));
      }
    }
  }
  return height * width - outsideTiles.union(moves).length;
}

void main() async {
  final lines = utf8.decoder
      .bind(File('puzzle_input.txt').openRead())
      .transform(const LineSplitter());
  var maze = <String>[];
  await for (final line in lines) {
    maze.add(line);
  }
  var start = findStart(maze);
  if (start == null) {
    print('No "S" found');
    return;
  }
  print('start = $start');
  final count = calculateInsideTileCount(maze, start);
  print('count = $count');
}

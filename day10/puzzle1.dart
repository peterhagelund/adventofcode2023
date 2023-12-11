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

int findFarthestPoint(List<String> maze, (int, int) start) {
  final height = maze.length;
  final width = maze[0].length;
  var queue = Queue.from([start]);
  var moves = Set.from([start]);
  while (queue.isNotEmpty) {
    final (y, x) = queue.removeFirst();
    final c = maze[y][x];
    if ((y > 0) &&
        'S|JL'.contains(c) &&
        '|7F'.contains(maze[y - 1][x]) &&
        !moves.contains((y - 1, x))) {
      moves.add((y - 1, x));
      queue.addLast((y - 1, x));
    }
    if ((y < height) &&
        'S|7F'.contains(c) &&
        '|JL'.contains(maze[y + 1][x]) &&
        !moves.contains((y + 1, x))) {
      moves.add((y + 1, x));
      queue.addLast((y + 1, x));
    }
    if ((x > 0) &&
        'S-J7'.contains(c) &&
        '-LF'.contains(maze[y][x - 1]) &&
        !moves.contains((y, x - 1))) {
      moves.add((y, x - 1));
      queue.addLast((y, x - 1));
    }
    if ((x < width) &&
        'S-LF'.contains(c) &&
        '-J7'.contains((maze[y][x + 1])) &&
        !moves.contains((y, x + 1))) {
      moves.add((y, x + 1));
      queue.addLast((y, x + 1));
    }
  }
  return moves.length ~/ 2;
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
  final count = findFarthestPoint(maze, start);
  print('count = $count');
}

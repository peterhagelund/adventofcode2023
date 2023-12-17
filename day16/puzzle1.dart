import 'dart:collection';
import 'dart:io';
import 'dart:convert';

enum Direction { right, down, left, up }

typedef Leg = (int, int, Direction);

int calculateEnergizedTiles(List<String> contraption, Leg start) {
  var legs = <Leg>{};
  final height = contraption.length;
  final width = contraption[0].length;
  var energized =
      List.generate(height, (_) => List.generate(width, (_) => false));
  var queue = Queue<Leg>();
  queue.addLast(start);
  while (queue.isNotEmpty) {
    final leg = queue.removeFirst();
    if (legs.contains(leg)) {
      continue;
    }
    legs.add(leg);
    var (y, x, direction) = leg;
    var done = false;
    while (!done) {
      energized[y][x] = true;
      final tile = contraption[y][x];
      switch (direction) {
        case Direction.right:
          if ('.-'.contains(tile)) {
            x++;
            if (x == width) {
              done = true;
            }
          } else {
            if (y > 0 && '|/'.contains(tile)) {
              queue.addLast((y - 1, x, Direction.up));
            }
            if (y + 1 < height && '|\\'.contains(tile)) {
              queue.addLast((y + 1, x, Direction.down));
            }
            done = true;
          }
        case Direction.down:
          if ('.|'.contains(tile)) {
            y++;
            if (y == height) {
              done = true;
            }
          } else {
            if (x > 0 && '-/'.contains(tile)) {
              queue.addLast((y, x - 1, Direction.left));
            }
            if (x + 1 < width && '-\\'.contains(tile)) {
              queue.addLast((y, x + 1, Direction.right));
            }
            done = true;
          }
        case Direction.left:
          if ('.-'.contains(tile)) {
            x--;
            if (x < 0) {
              done = true;
            }
          } else {
            if (y > 0 && '|\\'.contains(tile)) {
              queue.addLast((y - 1, x, Direction.up));
            }
            if (y + 1 < height && '|/'.contains(tile)) {
              queue.addLast((y + 1, x, Direction.down));
            }
            done = true;
          }
        case Direction.up:
          if ('.|'.contains(tile)) {
            y--;
            if (y < 0) {
              done = true;
            }
          } else {
            if (x > 0 && '-\\'.contains(tile)) {
              queue.addLast((y, x - 1, Direction.left));
            }
            if (x + 1 < width && '-/'.contains(tile)) {
              queue.addLast((y, x + 1, Direction.right));
            }
            done = true;
          }
      }
    }
  }
  var tile_count = 0;
  for (final row in energized) {
    for (final tile in row) {
      tile_count += (tile ? 1 : 0);
    }
  }
  return tile_count;
}

void main() async {
  final lines = utf8.decoder
      .bind(File('puzzle_input.txt').openRead())
      .transform(const LineSplitter());
  var contraption = <String>[];
  await for (final line in lines) {
    contraption.add(line);
  }
  final tile_count =
      calculateEnergizedTiles(contraption, (0, 0, Direction.right));
  print('energized tiles = $tile_count');
}

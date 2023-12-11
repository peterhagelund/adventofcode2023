import 'dart:io';
import 'dart:convert';

(List<int>, List<int>) getSpaceExpansion(List<String> space) {
  final height = space.length;
  final width = space[0].length;
  var rows = <int>[];
  var columns = <int>[];
  for (int y = 0; y < height; y++) {
    if ('.'.allMatches(space[y]).length == width) {
      rows.add(y);
    }
  }
  for (int x = 0; x < width; x++) {
    var count = 0;
    for (int y = 0; y < height; y++) {
      if (space[y][x] == '.') {
        count++;
      }
    }
    if (count == width) {
      columns.add(x);
    }
  }
  return (rows, columns);
}

Map<int, (int, int)> buildGalaxyMap(
    List<String> space, (List<int>, List<int>) expansion, int factor) {
  var map = <int, (int, int)>{};
  final rows = expansion.$1;
  final columns = expansion.$2;
  int n = 0;
  int _y = 0;
  for (int y = 0; y < space.length; y++) {
    if (rows.contains(y)) {
      _y += factor;
    } else {
      int _x = 0;
      for (int x = 0; x < space[y].length; x++) {
        if (columns.contains(x)) {
          _x += factor;
        } else {
          if (space[y][x] == '#') {
            map[n] = (_y, _x);
            n++;
          }
          _x++;
        }
      }
      _y++;
    }
  }
  return map;
}

List<(int, int)> buildGalaxyPairs(int count) {
  var pairs = <(int, int)>[];
  for (int g1 = 0; g1 < count; g1++) {
    for (int g2 = g1 + 1; g2 < count; g2++) {
      pairs.add((g1, g2));
    }
  }
  return pairs;
}

int calculateDistance(Map<int, (int, int)> map, (int, int) pair) {
  final pos1 = map[pair.$1]!;
  final pos2 = map[pair.$2]!;
  return (pos1.$1 - pos2.$1).abs() + (pos1.$2 - pos2.$2).abs();
}

void main() async {
  final lines = utf8.decoder
      .bind(File('puzzle_input.txt').openRead())
      .transform(const LineSplitter());
  var space = <String>[];
  await for (final line in lines) {
    space.add(line);
  }
  final expansion = getSpaceExpansion(space);
  final map = buildGalaxyMap(space, expansion, 1000000);
  final pairs = buildGalaxyPairs(map.length);
  var sum = 0;
  for (final pair in pairs) {
    final distance = calculateDistance(map, pair);
    sum += distance;
  }
  print('sum = $sum');
}

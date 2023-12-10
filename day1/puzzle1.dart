import 'dart:convert';
import 'dart:io';

void main() async {
  final lines = utf8.decoder
      .bind(File("puzzle_input.txt").openRead())
      .transform(const LineSplitter());
  final regex = RegExp(r'(\d)');
  int sum = 0;

  await for (final line in lines) {
    final matches = [
      for (final match in regex.allMatches(line)) int.parse(match.group(0)!)
    ];
    sum += matches.first * 10 + matches.last;
  }
  print('sum = $sum');
}

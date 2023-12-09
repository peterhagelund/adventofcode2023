import 'dart:convert';
import 'dart:io';
import 'dart:math';

/// Extrapolates the last value of the specified [List].
int extrapolate(List<int> values) {
  var sequences = <List<int>>[];
  var sequence = values;
  while (true) {
    sequences.add(sequence);
    if ((sequence.reduce(max) == 0) && (sequence.reduce(min) == 0)) {
      break;
    }
    var differences = <int>[];
    for (var i = 0; i < sequence.length - 1; i++) {
      differences.add(sequence[i + 1] - sequence[i]);
    }
    sequence = differences;
  }
  int last = 0;
  for (var i = sequences.length - 1; i >= 0; i--) {
    sequence = sequences[i];
    if (i == sequences.length - 1) {
      sequence.add(last);
    } else {
      last = sequence.last + last;
      sequence.add(last);
    }
  }
  return last;
}

/// Application entry-point.
void main() async {
  final lines = utf8.decoder
      .bind(File("puzzle_input.txt").openRead())
      .transform(const LineSplitter());
  int sum = 0;
  await for (final line in lines) {
    sum += extrapolate([for (final value in line.split(' ')) int.parse(value)]);
  }
  print('sum = $sum');
}

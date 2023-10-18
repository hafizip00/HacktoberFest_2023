extension Addition on String {
  String addA() {
    return this + "A";
  }
}

void main() {
  String x = "Try";
  print(x);
  print(x.addA());
}

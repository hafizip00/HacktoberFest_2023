void main() {
  // Create a list of numbers
  List<int> numbers = [1, 2, 3, 4, 5];

  // Use the map method to double each number in the list
  List<int> doubledNumbers = numbers.map((int number) {
    return number * 2;
  }).toList(); // Convert the result back to a list

  // Print the original and doubled numbers
  print("Original numbers: $numbers");
  print("Doubled numbers: $doubledNumbers");
}

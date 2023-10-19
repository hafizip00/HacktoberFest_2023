void pyramid(int n) {
  for (int i = 0; i < n; i++) {
    // Print spaces for the left-side of the pyramid
    for (int j = 0; j < n - i - 1; j++) {
      print(" ");
    }

    // Print asterisks for the left-side of the pyramid
    for (int k = 0; k <= i; k++) {
      print("* ");
    }

    // Move to the next row
    print("");
  }
}

void main(){
    pyramid(10);
}
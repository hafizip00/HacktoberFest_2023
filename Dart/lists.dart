// ignore_for_file: unused_local_variable

void main() {
  //Simple Creation of a list
  List initialized = ["item1", "item 2"];

  //Creation of a dynamic List
  //The compiler cannot infer what data type this list will hold
  List dynamic = [];

  //Creation of an unitialized list
  //Uninitialized List infer to have dynamic datatype by default if
  //not specified explicitly.
  List dynamicAndUninitialized;

  //Creation of a type aware list
  //The list doesn't have any elements in the list to infer what type it will
  //store but <String> generic that we have given to the List data type, helps
  // the compiler understand what data type this list will be holding.
  List<String> listOfStrings = [];

  //Iterating through a list

  //There are two things we do when we iterate through a list:
  //1. either we only look at each values and do something according to the
  //   value we have
  //  OR
  //2. change each value we have in the list.

  // Using forEach
  // We use forEach method of the list to iterate through the list and do some
  // task based on the value given

  List<int> exampleList = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
  ]; // we create a list with sample data

  exampleList.forEach((number) {
    print(number);
  });

  //Here, we are given an anonymous function which takes in a variable
  //called number. We use this function to tell the loop what to do using
  //every number we iterate over. Here for example, we iterate and print
  //each number.

  //Using map function
  //we use map function to change values in a list over an iterator and put
  //those changes to a new list by using the toList() method.

  exampleList = exampleList.map((number) => number = number + 1).toList();

  //Here, we are given an anonymous function which takes in a variable
  //called number. We use this function to tell the loop what to do using
  //every number we iterate over. Here for example, we iterate and increment
  //each number by one. After that we use the toList() method to collect the
  //changed values into a list and now we can either create a new list and
  //assign this collected data to that particular list or reassign the old
  //list variable again to that list;

  //Filtering values in a list
  //To search for values in a list we use the where() method.

  List<int> evenNumberList =
      exampleList.where((number) => number % 2 == 0).toList();

  // The where method gives us an anonymous function which takes in a variable
  // we need to return a condition here. It iterates through each number and if
  // that condiition satisfies if applied to the current number, only then we add it
  // to the list. in this case, we are looking for only even numbers so we check if
  // the remainder when dividing the number with 2 gives us 0 or not.
}

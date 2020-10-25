#include <vector>

int findOdd(const std::vector<int>& numbers){
  //your code here
  int counter = 0;
  for (size_t i = 0; i < numbers.size(); i++) {
    for (size_t j = 0; j < numbers.size(); j++) {
      if (numbers[i] == numbers[j]){
        counter++;
      }
    }
    if ((counter % 2) != 0){
      return numbers[i];
    }
    counter = 0;
  }
}

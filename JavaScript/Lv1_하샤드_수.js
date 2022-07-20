function solution(x) {
  var answer = false;
  let numSum = 0;
  let tempX = x;
  while (x > 0) {
    numSum += x % 10;
    x = parseInt(x / 10);
  }
  if (tempX % numSum == 0) {
    answer = true;
  }
  return answer;
}

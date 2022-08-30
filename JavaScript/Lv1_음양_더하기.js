function solution(absolutes, signs) {
  let answer = 0;
  absolutes.forEach((value, index) => {
    if (signs[index]) answer += value;
    else answer -= value;
  });
  return answer;
}

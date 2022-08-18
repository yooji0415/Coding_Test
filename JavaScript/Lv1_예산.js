function solution(d, budget) {
  const sortedD = d.sort((a, b) => {
    return a - b;
  });
  let answer = 0;
  sortedD.forEach((value) => {
    if(budget - value >= 0){
        answer++;
        budget -= value;
    }
  });
  return answer;
}

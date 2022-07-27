function solution(n) {
  var answer = [];
  let s = n.toString();
  for (let i = s.length; i > 0; i--) answer.push(parseInt(s.substr(i - 1, 1)));
  return answer;
}

function solution(n) {
  var answer = 0;
  var m = String(n);
  for (var i = 0; i < m.length; i++) {
    answer += parseInt(m[i]);
  }
  return answer;
}

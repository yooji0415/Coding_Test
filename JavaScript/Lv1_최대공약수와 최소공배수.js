function gcd(a, b) {
  const remainder = a % b;
  if (remainder === 0) return b;
  return gcd(b, remainder);
}

function solution(n, m) {
  var answer = [];
  var result = gcd(n, m);
  answer.push(result);
  answer.push((n * m) / result);
  return answer;
}

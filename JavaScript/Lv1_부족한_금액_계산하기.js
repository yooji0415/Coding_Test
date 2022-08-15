function solution(price, money, count) {
  let total = 0;
  for (let i = 1; i < count + 1; i++) total += i;
  total *= price;
  const answer = total - money;
  if (answer <= 0) return 0;
  return answer;
}

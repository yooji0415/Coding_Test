function solution(a, b) {
  let total = 0;
  const month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  const days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
  for (let i = 0; i < a; i++) total += month[i];
  total += b;
  return days[(total - 1) % 7];
}

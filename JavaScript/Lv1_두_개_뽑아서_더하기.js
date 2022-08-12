function solution(numbers) {
  const temp = [];
  for (let i = 1; i < numbers.length; i++) {
    for (let j = 0; j < i; j++) temp.push(numbers[i] + numbers[j]);
  }
  const uniq = [...new Set(temp)];
  uniq.sort((a, b) => {
    return a - b;
  });
  return uniq;
}

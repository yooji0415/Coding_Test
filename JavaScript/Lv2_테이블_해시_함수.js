function solution(data, col, row_begin, row_end) {
  var answer = 0;
  data.sort((a, b) => {
    let newA = a[col - 1];
    let newB = b[col - 1];
    if (newA === newB) {
      newA = a[0];
      newB = b[0];
      return newB - newA;
    }
    return newA - newB;
  });

  for (let i = row_begin - 1; i < row_end; i++)
    answer ^= data[i].reduce((acc, cur) => (acc += cur % (i + 1)), 0);

  return answer;
}

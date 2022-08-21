function solution(answers) {
  const supo1 = [1, 2, 3, 4, 5];
  const supo2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let cnt1 = 0;
  let cnt2 = 0;
  let cnt3 = 0;
  answers.forEach((value, index) => {
    if (supo1[index % 5] === value) cnt1 += 1;
    if (supo2[index % 8] === value) cnt2 += 1;
    if (supo3[index % 10] === value) cnt3 += 1;
  });
  const cntList = [cnt1, cnt2, cnt3];
  let answer = [];
  let maxCnt = -1;
  cntList.forEach((value, index) => {
    if (value > maxCnt) {
      maxCnt = value;
      answer = [index + 1];
    } else if (value === maxCnt) {
      answer.push(index + 1);
    }
  });
  return answer;
}

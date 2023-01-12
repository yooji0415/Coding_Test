const checkPalin = (startIdx, words, isEven) => {
  let answer = isEven ? 2 : 1;
  const len = words.length;
  let leftIdx = startIdx - 1;
  let rightIdx = isEven ? startIdx + 2 : startIdx + 1;
  while (leftIdx > -1 && rightIdx < len) {
    if (words[leftIdx] !== words[rightIdx]) break;
    answer += 2;
    leftIdx -= 1;
    rightIdx += 1;
  }
  return answer;
};

function solution(s) {
  let answer = 1;
  const words = s.split("");
  words.forEach((word, idx) => {
    if (idx < words.length - 1 && word === words[idx + 1])
      answer = Math.max(answer, checkPalin(idx, words, true));

    if (idx < words.length - 2 && word === words[idx + 2])
      answer = Math.max(answer, checkPalin(idx + 1, words, false));
  });
  return answer;
}

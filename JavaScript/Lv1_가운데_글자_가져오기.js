function solution(s) {
  const sLen = s.length;
  if (sLen === 1) return s;
  else if (sLen % 2 === 1) return s[(sLen - 1) / 2];
  else return s.slice((sLen - 2) / 2, sLen / 2 + 1);
}

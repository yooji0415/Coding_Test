function solution(s) {
  const lowerS = s.toLowerCase();
  const cntP = lowerS.split("p").length - 1;
  const cntY = lowerS.split("y").length - 1;
  if (cntP === cntY) return true;
  return false;
}

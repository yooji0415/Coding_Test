function solution(input_string) {
  let answer = "";
  const aloneAlpha = new Set();
  const alphaDict = {};

  [...input_string].forEach((val, idx) => {
    if (!alphaDict[val]) alphaDict[val] = [idx];
    else {
      const lastSeen = alphaDict[val][alphaDict[val].length - 1];
      if (idx - lastSeen > 1) aloneAlpha.add(val);
      alphaDict[val].push(idx);
    }
  });

  if (aloneAlpha.size === 0) return "N";
  return [...aloneAlpha].sort().join("");
}

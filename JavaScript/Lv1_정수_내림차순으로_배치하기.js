function solution(n) {
  var arr = (n + "").split("");
  arr.sort(function (a, b) {
    return b - a;
  });
  var answer = Number(arr.toString().replace(/\,/g, ""));
  return answer;
}

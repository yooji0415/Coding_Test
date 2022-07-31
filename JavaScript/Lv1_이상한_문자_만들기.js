function solution(s) {
  let ans = "";
  let temp = s.split(" ");
  for (let x of temp) {
    let arr = x.split("");
    let maparr = arr.map((c, idx) =>
      idx % 2 === 0 ? c.toUpperCase() : c.toLowerCase()
    );
    ans += maparr.join("") + " ";
  }
  return ans.slice(0, -1);
}

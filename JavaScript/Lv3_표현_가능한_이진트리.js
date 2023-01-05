function solution(numbers) {
  const answer = [];

  const checkFun = (n) => {
    console.log(`n: ${n}`);
    let binN = n.toString(2);

    let nodeCnt = 1;
    let c = 1;
    while (nodeCnt < binN.length) {
      nodeCnt = 2 ** c - 1;
      c++;
    }

    while (binN.length < nodeCnt) {
      binN = "0" + binN;
    }
    binN = "0" + binN;

    const tree = binN.split("").map((val) => parseInt(val));
    console.log(tree);
    const checkChild = (num) => {
      const orginalNum = num;
      let m = 1;
      let n = 0;
      while (num > 0) {
        if (num % 2 === 1) {
          m = num;
          break;
        }
        num /= 2;
        n++;
      }
      const [c1, c2] = [orginalNum - 2 ** (n - 1), orginalNum + 2 ** (n - 1)];
      console.log(`orginal: ${orginalNum} c1: ${c1} c2: ${c2}`);
      if (tree[c1] === 1 || tree[c2] === 1) return false;
      return true;
    };

    let result = true;
    for (let i = 1; i < tree.length; i++) {
      if (i % 2 === 1) continue;
      if (tree[i] === 0 && !checkChild(i)) {
        result = false;
        break;
      }
    }

    return result ? 1 : 0;
  };

  numbers.forEach((num) => {
    answer.push(checkFun(num));
  });
  return answer;
}

console.log(solution([7, 42, 5]));

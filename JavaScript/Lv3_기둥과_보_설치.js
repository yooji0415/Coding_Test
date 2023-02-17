function solution(n, build_frame) {
  const answer = [[]];

  const cols = Array.from(Array(n + 1), () => Array(n + 1).fill(false));
  const rows = Array.from(Array(n + 1), () => Array(n + 1).fill(false));

  console.log(cols);
  console.log(rows);

  const make = (frame) => {
    const [x, y, a, b] = frame;

    const makeCol = (x, y) => {
      y = n - y;
      // 바닥인 경우
      if (y === n) {
        cols[y][x] = true;
        cols[y - 1][x] = true;
        return;
      }
      // 다른 기둥 위
      if (cols[y][x]) {
        cols[y - 1][x] = true;
        return;
      }
      // 보의 한쪽 끝
      if (!rows[y][x]) return;
      if (x === 0 && !rows[y][x + 1]) return;
      if (x === n && !rows[y][x - 1]) return;
      let check = 0;
      if (rows[y][x + 1]) check++;
      if (rows[y][x - 1]) check++;
      if (check === 0 || check === 2) return;
      cols[y][x] = true;
      cols[y - 1][x] = true;
    };

    const makeRow = (x, y) => {
      y = n - y;
      if (y === n) return;
      if (x === n) return;
      // 보의 한쪽 끝
      let left = cols[y][x];
      let right = cols[y][x + 1];
      if (left || right) {
        rows[y][x] = true;
        rows[y][x + 1] = true;
        return;
      }
    };
  };

  return answer;
}

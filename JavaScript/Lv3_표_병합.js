function solution(commands) {
  let answer = [];
  const merged = [];
  const content = Array.from(Array(50), () => Array(50).fill("EMPTY"));

  for (let i = 0; i < 50; i++)
    merged.push(Array.from(Array(50), (_, idx) => [i, idx]));

  const updateByRC = (r, c, val) => {
    const [y1, x1] = merged[r][c];
    content[y1][x1] = val;
  };

  const updateByContent = (c1, c2) => {
    for (let y = 0; y < 50; y++) {
      for (let x = 0; x < 50; x++) {
        if (content[y][x] === c1) content[y][x] = c2;
      }
    }
  };

  const merge = (r1, c1, r2, c2) => {
    const [y1, x1] = merged[r1][c1];
    const [y2, x2] = merged[r2][c2];

    const content1 = content[y1][x1];
    const content2 = content[y2][x2];

    if (content1 === "EMPTY" && content2 !== "EMPTY")
      content[y1][x1] = content2;

    for (let y = 0; y < 50; y++) {
      for (let x = 0; x < 50; x++) {
        const [my, mx] = merged[y][x];
        if (my === y2 && mx === x2) merged[y][x] = [y1, x1];
      }
    }
  };

  const unmerge = (r, c) => {
    const [y1, x1] = merged[r][c];
    const tmp = content[y1][x1];

    for (let y = 0; y < 50; y++) {
      for (let x = 0; x < 50; x++) {
        const [my, mx] = merged[y][x];
        if (my === y1 && mx === x1) {
          merged[y][x] = [y, x];
          content[y][x] = "EMPTY";
        }
      }
    }
    content[r][c] = tmp;
  };

  const print = (r, c) => {
    const [y1, x1] = merged[r][c];
    const tmp = content[y1][x1];
    answer.push(tmp);
  };

  commands.forEach((c) => {
    const arr = c.split(" ");
    if (arr[0] === "UPDATE") {
      if (arr.length === 4)
        updateByRC(parseInt(arr[1]) - 1, parseInt(arr[2]) - 1, arr[3]);
      else updateByContent(arr[1], arr[2]);
    } else if (arr[0] === "MERGE")
      merge(
        parseInt(arr[1]) - 1,
        parseInt(arr[2]) - 1,
        parseInt(arr[3]) - 1,
        parseInt(arr[4]) - 1
      );
    else if (arr[0] === "UNMERGE")
      unmerge(parseInt(arr[1]) - 1, parseInt(arr[2]) - 1);
    else print(parseInt(arr[1]) - 1, parseInt(arr[2]) - 1);
  });

  return answer;
}

console.log(
  solution([
    "UPDATE 1 1 menu",
    "UPDATE 1 2 category",
    "UPDATE 2 1 bibimbap",
    "UPDATE 2 2 korean",
    "UPDATE 2 3 rice",
    "UPDATE 3 1 ramyeon",
    "UPDATE 3 2 korean",
    "UPDATE 3 3 noodle",
    "UPDATE 3 4 instant",
    "UPDATE 4 1 pasta",
    "UPDATE 4 2 italian",
    "UPDATE 4 3 noodle",
    "MERGE 1 2 1 3",
    "MERGE 1 3 1 4",
    "UPDATE korean hansik",
    "UPDATE 1 3 group",
    "UNMERGE 1 4",
    "PRINT 1 3",
    "PRINT 1 4",
  ])
);

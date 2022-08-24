function solution(array, commands) {
  const answer = [];
  commands.forEach((command) => {
    let splitArray = array.slice(command[0] - 1, command[1]);
    splitArray.sort((a, b) => {
      return a - b;
    });
    answer.push(splitArray[command[2] - 1]);
  });
  return answer;
}

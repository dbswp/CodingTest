// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');

// const A = parseInt(input[0], 10);
// const B = parseInt(input[1], 10);

const A = 1;
const B = 2;

console.log(A + B);

// 처럼 백준에서 제공하는 테스트 케이스를 입력하는 코드는 주석 처리 하시고 별도로 테스트 케이스를 직접 하셔서 테스트를 해보셔야 합니다.
// 그리고 백준 제출 시에는 반대로 입력하는 코드는 주석을 해제하고 테스트용으로 작성한 변수는 삭제하시고 제출 하시면 됩니다~!

const solution = (input) => {
  const [a, b] = (input + "").split(" ").map((s) => +s);
  return a + b;
};
process.stdin.on("data", (input) => console.log(solution(input)));
test("예제1", () => {
  const input = `1 2`;
  expect(solution(input)).toEqual(3);
});

// 구조분해 할당
// const user = {
//   name: "dbswp",
//   age: 30,
//   brain: 10,
// };
// const { name, age, brain } = user;
// console.log(name, age, brain);

//전개연산자
// const num = [1, 2, 5, 4, 8, 9, 6, 7];
// let sortNum = num.sort((a, b) => a - b);
// console.log(num);
// console.log(...num);
// console.log(sortNum);

// ...을 이용하여 문자열 -> 배열
let str = "apple";
let strToArr = [...str];
let strToArr1 = str.split("");
console.log(strToArr);
console.log(strToArr1);

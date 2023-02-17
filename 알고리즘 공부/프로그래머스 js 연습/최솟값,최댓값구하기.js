// // 실습1
// let num = [-1.23, 13, 14.52, -33.53, 30];
// num.sort((a, b) => a - b);
// console.log(Math.floor(num[0]), Math.floor(num[num.length - 1]));

// //실습2
// let sum = 0;
// let avg = 0;
// for (i of num) {
//   sum += Math.abs(i);
//   avg = sum / num.length;
// }
// console.log(avg);

// // 실습3
// console.log(Math.floor(Math.random() * 100));

let num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let plus = num.reduce((a, b) => a + b);
console.log(plus);

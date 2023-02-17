// // 실습;
// const arr = [];
// for (let i = 1; i < 101; i++) {
//   arr.push(i);
// }
// let sum = 0;
// arr.map((a) => (sum += a));

// console.log(arr);
// console.log(sum);

// const nums = [3, 6, 9, 12, 15, 18, 21];
// const nums1 = [1, 2, 3, 4, 5, 6];

// const divideArr = nums.map((item) => {
//   return item / 3;
// });
// const multipleArr = nums1.map((item) => {
//   return item * 4;
// });
// console.log(divideArr);
// console.log(multipleArr);

//실습 (filter, includs);
// let fruits1 = [
//   "사과",
//   "딸기",
//   "파인애플",
//   "수박",
//   "참외",
//   "오렌지",
//   "자두",
//   "망고",
// ];
// let fruits2 = ["수박", "사과", "참외", "오렌지", "파인애플", "망고"];

// const arr = [];
// const arr1 = [];

// // filter 사용
// const arr2 = fruits1.filter((item) => {
//   return fruits2.includes(item) ? arr.push(item) : arr1.push(item);
// });
// console.log(arr);
// console.log(arr1);

//reduce
// const number = [2, -5, -123, -5480, 24, 0, -69, 349, 3];
// const sumResult = number.reduce(
//   (acc, item, index, og) => {
//     item < 0 ? (acc[1] += 1) : (acc[0] += 1);
//     return acc;
//   },
//   [0, 0]
// );
// // acc의 초기값을 지정;
// console.log(sumResult);

//실습 reduce
// const arr = [];
// for (let i = 1; i < 101; i++) {
//   arr.push(i);
// }
// const sumResult = arr.reduce((acc, item, index, og) => {
//   return (acc += item);
// }, 0);
// console.log(sumResult);
